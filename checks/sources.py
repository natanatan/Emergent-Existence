"""The sources register and the evidence standard (docs/sources.md).

A source is anything a claim or hypothesis relies on from outside the book's
own derivations: a paper, a dataset, a proof, or a Computational Companion
run. Each is one record in registers/sources/EE-S-nnnn.yaml. Claims and
hypotheses cite them in a `sources` list, each citation with a role.

check(root, claims, hyps, add) runs the evidence-standard checks and reports
through the audit's add(check, subject, message).
"""
import datetime
import glob
import os

import yaml

ROLES = {"premise", "support", "lineage", "foil"}
KINDS = ["measurement", "replicated", "proof", "single-study", "simulation", "argument", "opinion"]
CURRENCY = {"current", "retracted", "failed-replication", "superseded"}

# The highest status an entry may hold, given the weakest kind of premise
# source it rests on. None means no cap from the source. Proposed defaults;
# the author sets the final table in docs/sources.md.
CAP = {
    "measurement": None,
    "replicated": None,
    "proof": None,
    "single-study": "Provisional",
    "simulation": "Provisional",
    "argument": "Provisional",
    "opinion": "Speculative",
}
# Statuses ordered by standing, for the cap. Statuses not listed (Open,
# Deferred, Rejected, Superseded) are not positive standings and are never capped.
STANDING = {"Speculative": 1, "Provisional": 2, "Derived": 3, "Retained": 3}
RECHECK_DAYS = 365

# How far along measurement -> model -> inference -> interpretation a citation
# is used (docs/sources.md, "Level"). Sources of these kinds may not carry a
# premise cited at mechanism or ontology without review.
LEVELS = ["observation", "effective", "mechanism", "ontology"]
LEVEL_CAPPED_KINDS = {"simulation", "argument", "opinion"}

CHECKS = [
    ("sources-resolve", "Sources resolve", "error"),
    ("status-capped", "Status capped by evidence", "error"),
    ("premise-checked", "Premise source checked", "review"),
    ("objection-recorded", "Strongest objection recorded", "review"),
    ("source-failed", "Premise source failed", "review"),
    ("currency-due", "Source due for recheck", "review"),
    ("single-line", "One line of evidence cited as several", "review"),
    ("level-exceeds-source", "Level exceeds source", "review"),
    ("degeneracy-recorded", "Degeneracy recorded", "review"),
]


def load(root):
    out = {}
    for p in sorted(glob.glob(os.path.join(root, "registers", "sources", "EE-S-*.yaml"))):
        with open(p, encoding="utf-8") as f:
            s = yaml.safe_load(f)
        out[s["id"]] = s
    return out


def _list(v):
    return v if isinstance(v, list) else ([] if v is None else [v])


def current_status(rec):
    hist = _list(rec.get("status_history"))
    return hist[-1].get("status") if hist else None


def _date(v):
    if isinstance(v, datetime.date):
        return v
    try:
        return datetime.date.fromisoformat(str(v))
    except ValueError:
        return None


def check(root, claims, hyps, add, today=None):
    today = today or datetime.date.today()
    sources = load(root)

    for sid, s in sources.items():
        if s.get("kind") not in KINDS:
            add("sources-resolve", sid, f"kind {s.get('kind')!r} is not one of {', '.join(KINDS)}")
        cur = s.get("currency") or {}
        if cur.get("status", "current") not in CURRENCY:
            add("sources-resolve", sid, f"currency status {cur.get('status')!r} is not one of {', '.join(sorted(CURRENCY))}")
        for d in _list(s.get("degeneracy")):
            if not isinstance(d, dict) or not (d.get("alternative") or "").strip():
                continue
            if not (d.get("discriminator") or "").strip():
                add("degeneracy-recorded", sid, f"degeneracy {d.get('alternative')!r} names no discriminator; an "
                                                "alternative counts only when it predicts a discriminable difference")
        checked = _date(cur.get("last_checked"))
        if checked is None or (today - checked).days > RECHECK_DAYS:
            add("currency-due", sid, f"currency last checked {cur.get('last_checked') or 'never'}; recheck for retractions, "
                                     "failed replications and superseding results")

    for rid, rec in list(claims.items()) + list(hyps.items()):
        cites = _list(rec.get("sources"))
        if not cites:
            continue
        premises = []
        for c in cites:
            sid, role = c.get("source"), c.get("role")
            if sid not in sources:
                add("sources-resolve", rid, f"cites source {sid}, which is not in registers/sources/")
                continue
            if role not in ROLES:
                add("sources-resolve", rid, f"cites {sid} with role {role!r}; roles are {', '.join(sorted(ROLES))}")
                continue
            level = c.get("level")
            if level is not None and level not in LEVELS:
                add("sources-resolve", rid, f"cites {sid} at level {level!r}; levels are {', '.join(LEVELS)}")
                continue
            if role != "premise":
                continue
            premises.append(sources[sid])
            chk = c.get("checked") or {}
            missing = [k for k, ok in (("cited_for", c.get("cited_for")), ("locator", c.get("locator")),
                                       ("checked.date", chk.get("date")), ("checked.by", chk.get("by"))) if not ok]
            if missing:
                add("premise-checked", rid, f"premise {sid} is missing {', '.join(missing)}")
            if not sources[sid].get("strongest_objection"):
                add("objection-recorded", rid, f"premise {sid} has no strongest objection recorded beside it")
            kind = sources[sid].get("kind")
            if level in ("mechanism", "ontology") and kind in LEVEL_CAPPED_KINDS:
                add("level-exceeds-source", rid, f"premise {sid} ({kind}) is cited at level {level}; a {kind} "
                                                 "supports an effective description, not a claim about what exists")
            if level == "ontology":
                if "degeneracy" not in sources[sid]:
                    add("degeneracy-recorded", rid, f"premise {sid} is cited at level ontology; record its known "
                                                    "degeneracies, or an empty list if none is known")
            state = (sources[sid].get("currency") or {}).get("status", "current")
            if state != "current":
                add("source-failed", rid, f"premise {sid} is {state}; the author reviews every claim resting on it")

        # status is capped by the weakest premise
        status = current_status(rec)
        if status in STANDING and premises:
            caps = [(CAP.get(p.get("kind")), p) for p in premises if CAP.get(p.get("kind"))]
            if caps:
                cap, weakest = min(caps, key=lambda x: STANDING[x[0]])
                if STANDING[status] > STANDING[cap]:
                    add("status-capped", rid, f"status {status} exceeds {cap}, the most that premise "
                                              f"{weakest['id']} ({weakest.get('kind')}) allows")

        # several sources from one line of evidence are one line
        lines = {}
        for c in cites:
            s = sources.get(c.get("source"))
            if s and c.get("role") in ("premise", "support"):
                lines.setdefault(s.get("line") or s["id"], []).append(s["id"])
        for line, ids in lines.items():
            if len(ids) > 1:
                add("single-line", rid, f"{', '.join(ids)} are one line of evidence ({line}); count them once")
    return sources
