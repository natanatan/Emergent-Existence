"""Claim tags in the manuscript source (style sheet, 2a).

Each claim's derivation or statement carries an invisible tag, placed
immediately before the line where it begins:

    <!-- EE-C-nnnn derivation -->   or   <!-- EE-C-nnnn statement -->

Tags never print. The build checks that every tag matches the register and
every register entry has its tag. A tag identifies the claim occurrence, not
its printed position: moving a claim changes only its appearance metadata.

The check is dormant until the manuscript holds at least one tag, so the
section stubs imported before the text arrives raise nothing.
"""
import glob
import os
import re

TAG = re.compile(r"<!--\s*(EE-C-\d{4})\s+(derivation|statement)\s*-->")
HEADING = re.compile(r"^#\s+(\d+\.\d+)\b", re.M)
STATED_KINDS = {"test", "forward_pointer"}

CHECKS = [
    ("claim-tags", "Claim tags match the register", "error"),
    ("claim-tag-section", "Claim tag in a different section", "review"),
]


def scan(root):
    tags = []
    for path in sorted(glob.glob(os.path.join(root, "manuscript", "**", "*.md"), recursive=True)):
        text = open(path, encoding="utf-8").read()
        h = HEADING.search(text)
        section = h.group(1) if h else None
        rel = os.path.relpath(path, root)
        for m in TAG.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            tags.append({"claim": m.group(1), "role": m.group(2), "section": section, "where": f"{rel}:{line}"})
    return tags


def manuscript_edition(editions):
    marked = [e for e, rec in editions.items() if rec.get("manuscript")]
    if marked:
        return marked[0]
    return max(editions, key=lambda e: str(editions[e].get("released") or "")) if editions else None


def check(root, claims, editions, add):
    """Returns True when the check ran (the manuscript holds tags)."""
    tags = scan(root)
    if not tags:
        return False
    ed = manuscript_edition(editions)
    seen = {}
    for t in tags:
        cid, role = t["claim"], t["role"]
        c = claims.get(cid)
        if c is None:
            add("claim-tags", cid, f"tagged at {t['where']}, but no such claim is registered")
            continue
        if c.get("merged_into"):
            add("claim-tags", cid, f"tagged at {t['where']}, but it was merged into {c['merged_into']}; tag the survivor")
            continue
        want = "statement" if c.get("kind") in STATED_KINDS else "derivation"
        if role != want:
            add("claim-tags", cid, f"tagged as {role} at {t['where']}; a {c.get('kind')} claim is tagged as {want}")
        if (cid, role) in seen:
            add("claim-tags", cid, f"tagged twice as {role}: {seen[(cid, role)]} and {t['where']}")
        seen[(cid, role)] = t["where"]
        app = next((a for a in c.get("appearances") or []
                    if a.get("edition") == ed and a.get("role") == role), None)
        if app and app.get("section") and t["section"] and str(app["section"]) != t["section"]:
            add("claim-tag-section", cid, f"tag is in {t['section']} ({t['where']}); the register places its {role} "
                                          f"in {app['section']}. Update the appearance metadata, not the ID")
    for cid, c in claims.items():
        if c.get("merged_into"):
            continue
        for a in c.get("appearances") or []:
            if a.get("edition") == ed and a.get("role") in ("derivation", "statement") and (cid, a["role"]) not in seen:
                add("claim-tags", cid, f"has a {a['role']} in {ed} ({a.get('section') or a.get('location')}) but no tag in the manuscript")
    return True
