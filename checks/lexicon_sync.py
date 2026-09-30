#!/usr/bin/env python3
"""One-way sync from the element table to the Linking Lexicon page.

registers/elements/elements.yaml is the source. The Lexicon page is a view of
it that also holds richer material (formulas, readings, notes, links the table
does not record), so this script only adds: every element whose lexicon_id is
not yet a node becomes a node, with an `introduced` link from its stage and a
`requires` link from each element it requires. It never edits or removes an
existing node, and it reports any drift between the two for review.

Usage: python checks/lexicon_sync.py LEXICON(.json|.html) -o OUT [--rev N]
An .html input is the published Lexicon page; its embedded data is replaced.
"""
import argparse
import datetime
import json
import os
import re
import sys

import yaml

DATA_RE = re.compile(r'(<script type="application/json" id="lexicon-data">)(.*?)(</script>)', re.S)


def sync(lex, elements):
    by_code = {e["code"]: e for e in elements}
    nodes = {n["id"]: n for n in lex["nodes"]}
    links = {(l["from"], l["to"], l["type"]) for l in lex["links"]}
    added, drift = [], []
    for e in elements:
        nid = e["lexicon_id"]
        if nid in nodes:
            if nodes[nid].get("code") != e["code"]:
                drift.append(f"{nid}: code {nodes[nid].get('code')!r} on the page, {e['code']!r} in the table")
            continue
        stage = by_code[e["row"]]["lexicon_id"]
        syms = e.get("symbols") or []
        node = {"id": nid, "label": e["label"], "code": e["code"], "kind": e.get("kind", "term"),
                "stage": stage, "volume": e.get("volume"), "chapter": e.get("chapter"),
                "section": e.get("section"), "status": e.get("status", ""),
                "symbol": syms[0] if syms else "", "definition": e.get("definition", ""), "note": "",
                "symbols": syms}
        lex["nodes"].append(node)
        nodes[nid] = node
        added.append(e["code"])
        new = [(stage, nid, "introduced")] + [(by_code[r]["lexicon_id"], nid, "requires")
                                              for r in e.get("requires") or [] if r in by_code]
        for f, t, ty in new:
            if (f, t, ty) not in links:
                links.add((f, t, ty))
                lex["links"].append({"from": f, "to": t, "type": ty})
    table_ids = {e["lexicon_id"] for e in elements}
    for n in lex["nodes"]:
        if n["id"] not in table_ids:
            drift.append(f"{n['id']}: on the page but not in the element table")
    return added, drift


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lexicon")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--rev", type=int)
    ap.add_argument("--root", default=".")
    a = ap.parse_args()
    raw = open(a.lexicon, encoding="utf-8").read()
    is_html = a.lexicon.endswith(".html")
    lex = json.loads(DATA_RE.search(raw).group(2) if is_html else raw)
    table = yaml.safe_load(open(os.path.join(a.root, "registers", "elements", "elements.yaml"), encoding="utf-8"))
    added, drift = sync(lex, table["elements"])
    if added:
        meta = lex.setdefault("meta", {})
        meta["rev"] = a.rev or (meta.get("rev", 0) + 1)
        meta["updated"] = datetime.date.today().isoformat()
        meta["note"] = (f"Synced from the element table in the Emergent-Existence repository: {len(added)} "
                        f"elements added ({', '.join(added)}). The table is the source; this page is a view of it.")
    text = json.dumps(lex, ensure_ascii=False, indent=1)
    if is_html:
        text = DATA_RE.sub(lambda m: m.group(1) + text.replace("</", "<\\/") + m.group(3), raw, count=1)
    open(a.out, "w", encoding="utf-8").write(text)
    print(f"added {len(added)} nodes: {' '.join(added) or '-'}")
    for d in drift:
        print("drift: " + d)
    return 0


if __name__ == "__main__":
    sys.exit(main())
