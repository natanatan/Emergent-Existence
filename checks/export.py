#!/usr/bin/env python3
"""Generate exports/ from the registers.

exports/ is what the other projects read (the Computational Companion and
Emergent World); they never parse the manuscript. Files are deterministic:
running this twice on the same registers gives byte-identical output, so the
audit can check that exports/ is current.

Usage: python checks/export.py [--root .] [--check]
  --check  exit 1 if exports/ differs from what the registers would generate
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit import as_list, load  # noqa: E402

SCHEMA = "emergent-existence-exports/1"


def latest_status(rec):
    hist = as_list(rec.get("status_history"))
    return hist[-1]["status"] if hist else None


def latest_version(c):
    versions = c.get("versions") or {}
    if not versions:
        return None, None
    key = sorted(versions, key=lambda k: int(str(k).lstrip("v") or 0))[-1]
    return key, versions[key]


def build(root):
    claims, hyps, editions, elements, ledgers = load(root)
    merged = {cid: c["merged_into"] for cid, c in claims.items() if c.get("merged_into")}

    out_claims = []
    for cid in sorted(claims):
        c = claims[cid]
        if cid in merged:
            continue
        vkey, v = latest_version(c)
        out_claims.append({
            "id": cid,
            "kind": c.get("kind"),
            "use": c.get("use"),
            "status": latest_status(c),
            "text": (v or {}).get("text"),
            "version": vkey,
            "aliases": as_list(c.get("aliases")),
            "dependencies": [d["claim"] for d in as_list(c.get("dependencies"))],
            "relations": [{"type": r["type"], "claim": r["claim"]} for r in as_list(c.get("relations"))],
            "concepts": as_list(c.get("concepts")),
            "composition": as_list(c.get("composition")),
            "appearances": [{k: a.get(k) for k in ("edition", "role", "chapter", "section", "label", "type_word", "cites")
                             if a.get(k) is not None} for a in as_list(c.get("appearances"))],
        })

    out_hyps = []
    for hid in sorted(hyps):
        h = hyps[hid]
        out_hyps.append({
            "id": hid,
            "aliases": as_list(h.get("aliases")),
            "hypothesis": h.get("hypothesis"),
            "status": latest_status(h),
            "status_text": h.get("status_text"),
            "resolve_by": h.get("resolve_by"),
            "revisited_in": h.get("revisited_in"),
            "companion_testable": bool(h.get("companion_testable")),
        })

    out_elements = [elements[k] for k in sorted(elements)]

    # the earned ladder: stages in order, what each earns and withholds
    stage_codes = [e["code"] for e in sorted(
        (e for e in elements.values() if e.get("kind") in ("foundation", "stage") and e.get("row") == e["code"]),
        key=lambda e: (e.get("order") or 999, e["code"]))]
    ledger_by_stage = {led["stage"]: led for led in ledgers}
    ladder, earned = [], []
    for code in stage_codes:
        st = elements[code]
        introduced = sorted(e["code"] for e in elements.values()
                            if e.get("row") == code and e["code"] != code)
        led = ledger_by_stage.get(code, {})
        new = [code] + introduced
        earned = earned + [x for x in new if x not in earned]
        ladder.append({
            "stage": code,
            "title": st.get("label"),
            "volume": st.get("volume"),
            "book": st.get("book"),
            "chapter": st.get("chapter"),
            "planned": "planned" in str(st.get("status", "")).lower(),
            "earns": new,
            "earned_so_far": list(earned),
            "earns_text": [e.get("item") for e in as_list(led.get("earns"))],
            "withholds": [{k: w.get(k) for k in ("item", "deferred_to", "scope") if w.get(k) is not None}
                          for w in as_list(led.get("withholds"))],
        })

    backlog = [h for h in out_hyps if h["companion_testable"]]
    manifest = {
        "schema": SCHEMA,
        "editions": sorted(editions),
        "counts": {"claims": len(out_claims), "hypotheses": len(out_hyps), "elements": len(out_elements),
                   "stages": len(ladder), "companion_backlog": len(backlog), "merged_ids": len(merged)},
        "merged_ids": dict(sorted(merged.items())),
        "files": ["claims.json", "hypotheses.json", "elements.json", "ladder.json", "companion-backlog.json"],
    }
    return {
        "manifest.json": manifest,
        "claims.json": out_claims,
        "hypotheses.json": out_hyps,
        "elements.json": out_elements,
        "ladder.json": ladder,
        "companion-backlog.json": backlog,
    }


def render(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=False) + "\n"


def stale_files(root):
    """Names of export files that differ from what the registers generate."""
    out = []
    for name, obj in build(root).items():
        path = os.path.join(root, "exports", name)
        cur = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if cur != render(obj):
            out.append(name)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        stale = stale_files(a.root)
        if stale:
            print("exports/ is out of date: " + ", ".join(stale) + ". Run python checks/export.py")
            return 1
        print("exports/ is current")
        return 0
    os.makedirs(os.path.join(a.root, "exports"), exist_ok=True)
    for name, obj in build(a.root).items():
        with open(os.path.join(a.root, "exports", name), "w", encoding="utf-8") as f:
            f.write(render(obj))
    print("wrote exports/: " + ", ".join(sorted(build(a.root))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
