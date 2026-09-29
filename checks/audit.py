#!/usr/bin/env python3
"""Audit the registers against the claims model (docs/claims-model.md).

Writes build/audit/report.json and build/audit/report.md.
Exit status is 1 when any error is open, 0 otherwise.

Usage: python checks/audit.py [--root .] [--out build/audit]
"""
import argparse
import collections
import datetime
import glob
import json
import os
import sys

import yaml

STATUSES = {"Retained", "Provisional", "Derived", "Open", "Deferred", "Rejected", "Speculative", "Superseded"}
ROLES = {"derivation", "statement", "foreshadowing", "restatement"}
STATED_KINDS = {"test", "forward_pointer"}   # stated, never derived
RELATION_TYPES = {"derives_from", "supersedes", "refines", "equivalent_to", "contrasts_with", "generalizes",
                  "specializes", "foreshadows", "diagnoses", "tests", "represents"}
USES = {"constitutive", "representational", "diagnostic"}

# (check id, title, level) in report order
CHECKS = [
    ("references", "References resolve", "error"),
    ("cycles", "No circular dependency", "error"),
    ("earned-order", "Earned order", "error"),
    ("interpretation-premise", "Interpretation is not a premise", "error"),
    ("composition", "Composition matches dependencies", "error"),
    ("labels-unique", "Labels unique per edition", "error"),
    ("one-derivation", "One derivation per claim", "error"),
    ("only-derivations-labelled", "Only derivations are labelled", "error"),
    ("citations", "Citations resolve", "error"),
    ("superseded-out", "Superseded claims stay out", "error"),
    ("status-history", "Status history is well formed", "error"),
    ("superseded-dependency", "Superseded dependency", "review"),
    ("correction", "Correction recorded", "review"),
    ("withholdings", "Withholdings accounted for", "review"),
    ("unmapped", "Claim not mapped to elements", "review"),
    ("unclassified-use", "Use not classified", "review"),
]
PENDING = [
    "Untyped later reference (needs the manuscript text in the repository)",
    "Labels map to claims (needs the manuscript text in the repository)",
    "Composition change recorded (needs register history across runs)",
    "Released editions frozen (needs register history across runs)",
]


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load(root):
    reg = os.path.join(root, "registers")
    claims = {}
    for p in sorted(glob.glob(os.path.join(reg, "claims", "*.yaml"))):
        c = load_yaml(p)
        claims[c["id"]] = c
    hyps = {}
    for p in sorted(glob.glob(os.path.join(reg, "hypotheses", "*.yaml"))):
        h = load_yaml(p)
        hyps[h["id"]] = h
    editions = {}
    for p in sorted(glob.glob(os.path.join(reg, "editions", "*.yaml"))):
        e = load_yaml(p)
        editions[e["id"]] = e
    elements = {}
    ep = os.path.join(reg, "elements", "elements.yaml")
    if os.path.exists(ep):
        for e in load_yaml(ep)["elements"]:
            elements[e["code"]] = e
    ledgers = [load_yaml(p) for p in sorted(glob.glob(os.path.join(reg, "ledgers", "*.yaml")))]
    return claims, hyps, editions, elements, ledgers


def as_list(v):
    return v if isinstance(v, list) else ([] if v is None else [v])


def dep_ids(c):
    return [d["claim"] for d in as_list(c.get("dependencies"))]


def rel(c, *types):
    return [r["claim"] for r in as_list(c.get("relations")) if r.get("type") in types]


def audit(root):
    claims, hyps, editions, elements, ledgers = load(root)
    findings = []

    def add(check, subject, message):
        findings.append({"check": check, "subject": subject, "message": message,
                         "key": f"{check}|{subject}|{message}"})

    # chapter of each claim in each edition: its derivation, else its first appearance
    def chapter_in(c, edition):
        apps = [a for a in as_list(c.get("appearances")) if a.get("edition") == edition]
        der = [a for a in apps if a.get("role") == "derivation"]
        pick = der or apps
        return pick[0].get("chapter") if pick else None

    # merged claims: a retired duplicate points to the claim that absorbed it
    merged = {cid: c["merged_into"] for cid, c in claims.items() if c.get("merged_into")}
    for cid, target in merged.items():
        if target not in claims:
            add("references", cid, f"merged into {target}, which does not exist")
        elif cid not in as_list(claims[target].get("aliases")):
            add("references", cid, f"merged into {target}, which does not list it as an alias")
        if as_list(claims[cid].get("appearances")):
            add("references", cid, "retired by merge but still has appearances")
    for cid, c in claims.items():
        for d in dep_ids(c) + [r.get("claim") for r in as_list(c.get("relations"))]:
            if d in merged:
                add("references", cid, f"points to {d}, which was merged into {merged[d]}")
    active = {cid: c for cid, c in claims.items() if cid not in merged}

    # references
    for cid, c in active.items():
        for d in dep_ids(c):
            if d not in claims:
                add("references", cid, f"dependency {d} does not exist")
        for r in as_list(c.get("relations")):
            if r.get("type") not in RELATION_TYPES:
                add("references", cid, f"unknown relation type {r.get('type')}")
            if r.get("claim") not in claims and r.get("claim") not in hyps:
                add("references", cid, f"relation target {r.get('claim')} does not exist")
        if c.get("use") is None and cid not in merged:
            add("unclassified-use", cid, "use not yet classified (constitutive, representational or diagnostic)")
        elif c.get("use") not in USES:
            add("references", cid, f"use must be one of {sorted(USES)}")
        for code in as_list(c.get("concepts")) + as_list(c.get("composition")):
            if code not in elements:
                add("references", cid, f"element {code} does not exist")
        versions = c.get("versions") or {}
        for a in as_list(c.get("appearances")):
            if a.get("edition") not in editions:
                add("references", cid, f"edition {a.get('edition')} does not exist")
            if a.get("version") not in versions:
                add("references", cid, f"appearance points to missing version {a.get('version')}")
            if a.get("role") is not None and a.get("role") not in ROLES:
                add("references", cid, f"unknown appearance role {a.get('role')}")

    # cycles in the dependency graph
    state = {}

    def visit(n, stack):
        state[n] = 1
        stack.append(n)
        for m in dep_ids(claims[n]):
            if m not in claims:
                continue
            if state.get(m) == 1:
                cyc = stack[stack.index(m):] + [m]
                add("cycles", n, " → ".join(cyc))
            elif m not in state:
                visit(m, stack)
        stack.pop()
        state[n] = 2

    sys.setrecursionlimit(10000)
    for n in claims:
        if n not in state:
            visit(n, [])

    # earned order, per edition
    for cid, c in claims.items():
        eds = {a.get("edition") for a in as_list(c.get("appearances"))}
        for ed in eds:
            ch = chapter_in(c, ed)
            if ch is None:
                continue
            for d in dep_ids(c) + rel(c, "derives_from"):
                if d in claims:
                    dch = chapter_in(claims[d], ed)
                    if dch is not None and dch > ch:
                        add("earned-order", cid, f"{ed}: depends on {d}, which is earned later (chapter {dch} > {ch})")
            for code in as_list(c.get("composition")):
                ech = (elements.get(code) or {}).get("chapter")
                if ed.startswith("book-1/") and ech is not None and ech > ch:
                    add("earned-order", cid, f"{ed}: composition uses {code}, earned in chapter {ech} > {ch}")

    # interpretation is not a premise
    for cid, c in claims.items():
        for d in dep_ids(c):
            if d in claims and claims[d].get("use") == "representational":
                add("interpretation-premise", cid, f"depends on {d}, whose use is representational")

    # composition = union of the concepts of the dependencies
    for cid, c in active.items():
        if not as_list(c.get("concepts")):
            add("unmapped", cid, "no element concepts recorded")
        derived = set()
        for d in dep_ids(c):
            if d in claims:
                derived |= set(as_list(claims[d].get("concepts")))
        if set(as_list(c.get("composition"))) != derived:
            add("composition", cid, f"composition {sorted(as_list(c.get('composition')))} "
                                    f"≠ derived {sorted(derived)}")

    # appearances and labels
    by_ed = collections.defaultdict(list)
    for cid, c in claims.items():
        for a in as_list(c.get("appearances")):
            by_ed[a.get("edition")].append((cid, a))
    for ed, apps in by_ed.items():
        labels = collections.defaultdict(list)
        for cid, a in apps:
            if a.get("role") == "derivation" and a.get("label"):
                labels[str(a["label"])].append(cid)
        for cid, a in apps:
            if a.get("role") == "statement" and a.get("label"):
                labels[str(a["label"])].append(cid)
        for lab, cids in labels.items():
            if len(set(cids)) > 1:
                add("labels-unique", f"{ed} {lab}", "shared by " + ", ".join(sorted(set(cids))))
        per_claim = collections.defaultdict(list)
        for cid, a in apps:
            per_claim[cid].append(a)
        labelled = {cid for cid, a in apps if a.get("role") in ("derivation", "statement") and a.get("label")}
        for cid, al in per_claim.items():
            stated = claims[cid].get("kind") in STATED_KINDS
            want, other = ("statement", "derivation") if stated else ("derivation", "statement")
            n = sum(1 for a in al if a.get("role") == want)
            if n == 0:
                add("one-derivation", cid, f"{ed}: no {want} appearance assigned")
            elif n > 1:
                add("one-derivation", cid, f"{ed}: {n} {want} appearances")
            if any(a.get("role") == other for a in al):
                add("one-derivation", cid, f"{ed}: a {claims[cid].get('kind') or 'claim'} cannot have a {other} appearance")
            for a in al:
                if a.get("role") in ("foreshadowing", "restatement"):
                    if a.get("label"):
                        add("only-derivations-labelled", cid, f"{ed}: {a['role']} carries label {a['label']}")
                    if a.get("cites") and str(a["cites"]) not in labels:
                        add("citations", cid, f"{ed}: cites {a['cites']}, which is not a derivation or statement label")
                    if not a.get("cites") and cid in labelled:
                        add("citations", cid, f"{ed}: {a['role']} does not cite the label of its derivation or statement")
        released = (editions.get(ed) or {}).get("released")
        for cid, al in per_claim.items():
            c = claims[cid]
            if as_list(c.get("superseded_by")) or rel_superseded(claims, cid):
                if not any(a.get("historical") for a in al) and ed != first_edition(c):
                    add("superseded-out", cid, f"superseded, but printed in {ed} (released {released})")

    # status history
    for cid, c in list(claims.items()) + list(hyps.items()):
        for ev in as_list(c.get("status_history")):
            if ev.get("status") not in STATUSES or not ev.get("date") or not ev.get("reason"):
                add("status-history", cid, f"malformed status event {ev}")

    # superseded dependency (review)
    for cid, c in claims.items():
        for d in dep_ids(c):
            if d in claims and rel_superseded(claims, d):
                add("superseded-dependency", cid, f"still depends on superseded {d}")

    # corrections (review)
    for cid, c in claims.items():
        for ev in as_list(c.get("history")):
            if ev.get("kind") == "correction" and not ev.get("reviewed"):
                add("correction", cid, f"dependency correction on {ev.get('date')}: {ev.get('note', '')}")

    # withholdings (review)
    for led in ledgers:
        for w in as_list(led.get("withholds")):
            if not w.get("deferred_to") and not w.get("scope"):
                add("withholdings", led.get("stage"), f"'{w.get('item')}' names no destination and is not marked beyond the series or open")

    return findings, claims, hyps, editions, elements


def rel_superseded(claims, cid):
    """True when another claim declares that it supersedes cid."""
    return any(cid in [r["claim"] for r in as_list(c.get("relations")) if r.get("type") == "supersedes"]
               for c in claims.values())


def first_edition(c):
    eds = [v.get("edition") for v in (c.get("versions") or {}).values()]
    return eds[0] if eds else None


def render(findings, claims, hyps, editions, elements):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    by = collections.defaultdict(list)
    for f in findings:
        by[f["check"]].append(f)
    errors = sum(len(by[c]) for c, _, lvl in CHECKS if lvl == "error")
    reviews = sum(len(by[c]) for c, _, lvl in CHECKS if lvl == "review")
    missing = len({f["subject"] for f in by["one-derivation"] if "appearance assigned" in f["message"]})
    lines = [
        f"**{errors} open errors · {reviews} review flags** · {len(claims)} claims · {len(hyps)} hypotheses · "
        f"{len(elements)} elements · {len(editions)} editions",
        "",
        f"Claims still missing a derivation (or, for tests and forward pointers, a statement) appearance: **{missing}**",
        "",
        "| Check | Level | Open |",
        "| --- | --- | --- |",
    ]
    for cid, title, lvl in CHECKS:
        lines.append(f"| {title} | {'Error' if lvl == 'error' else 'Review'} | {len(by[cid])} |")
    for cid, title, lvl in CHECKS:
        items = by[cid]
        if not items:
            continue
        lines += ["", f"<details><summary><b>{title}</b> ({len(items)})</summary>", ""]
        msgs = collections.Counter(f["message"] for f in items)
        common, n = msgs.most_common(1)[0]
        if len(items) > 20 and n > len(items) / 2:
            # one message shared by most findings: list the subjects compactly
            subs = [f["subject"] for f in items if f["message"] == common]
            lines.append(f"{common}: " + ", ".join(f"`{s}`" for s in subs[:400]) + (" …" if len(subs) > 400 else ""))
            items = [f for f in items if f["message"] != common]
            lines.append("")
        for f in items[:80]:
            lines.append(f"- `{f['subject']}` {f['message']}")
        if len(items) > 80:
            lines.append(f"- … and {len(items) - 80} more (full list in report.json)")
        lines += ["", "</details>"]
    lines += ["", "Not yet checked: " + "; ".join(PENDING) + ".", "", f"_Run {now}_"]
    return "\n".join(lines), {"errors": errors, "reviews": reviews, "missing_derivations": missing}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default="build/audit")
    a = ap.parse_args()
    findings, claims, hyps, editions, elements = audit(a.root)
    md, summary = render(findings, claims, hyps, editions, elements)
    os.makedirs(a.out, exist_ok=True)
    level = {c: lvl for c, _, lvl in CHECKS}
    for f in findings:
        f["level"] = level[f["check"]]
    with open(os.path.join(a.out, "report.json"), "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "findings": findings}, f, ensure_ascii=False, indent=1)
    with open(os.path.join(a.out, "report.md"), "w", encoding="utf-8") as f:
        f.write(md + "\n")
    print(md.split("\n")[0])
    return 1 if summary["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
