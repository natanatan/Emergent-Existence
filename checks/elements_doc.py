#!/usr/bin/env python3
"""Generate docs/elements.md from registers/elements/elements.yaml.

Usage: python checks/elements_doc.py [--root .] [--check]
  --check  exit 1 if docs/elements.md differs from what the table generates
"""
import argparse
import os
import sys

import yaml

HEAD = """# Element table

The concepts of the Linking Lexicon, each with a two-letter code. Rows are conceptual stages, like the periods of a periodic table. Stage is conceptual and chapter is editorial: the chapter shown is where that stage is currently developed, and codes never change if chapters are reordered. Generated from [`registers/elements/elements.yaml`](../registers/elements/elements.yaml); do not edit by hand.
"""
ROMAN = {1: "I", 2: "II", 3: "III"}


def where(e):
    if e.get("volume") == 1 and e.get("book") == 1 and e.get("chapter"):
        return "Ch. %s" % e["chapter"]
    if e.get("volume") == 1:
        return "Book %s" % ROMAN.get(e.get("book"), e.get("book"))
    return "Vol. %s" % ROMAN.get(e.get("volume"), e.get("volume"))


def render(elements):
    by_code = {e["code"]: e for e in elements}
    stages = sorted((e for e in elements if e.get("row") == e["code"]),
                    key=lambda e: (e.get("order") or 999, e["code"]))
    found = [e for e in elements if e.get("kind") == "foundation"]
    out = [HEAD, "**Foundations:** " + " · ".join(
        "`%s` %s (%s)" % (e["code"], e["label"], min(e.get("symbols") or [""], key=len)) for e in found), "",
        "| Row | Stage | Elements |", "| --- | --- | --- |"]
    for st in stages:
        members = [e for e in elements if e.get("row") == st["code"] and e["code"] != st["code"]]
        cells = " · ".join("`%s` %s" % (e["code"], e["label"]) for e in members) or "—"
        out.append("| `%s` | %s (%s) | %s |" % (st["code"], st["label"], where(st), cells))
    assert all(e.get("row") in by_code for e in elements)
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    src = os.path.join(a.root, "registers", "elements", "elements.yaml")
    dst = os.path.join(a.root, "docs", "elements.md")
    text = render(yaml.safe_load(open(src, encoding="utf-8"))["elements"])
    if a.check:
        cur = open(dst, encoding="utf-8").read() if os.path.exists(dst) else None
        if cur != text:
            print("docs/elements.md is out of date. Run python checks/elements_doc.py")
            return 1
        print("docs/elements.md is current")
        return 0
    open(dst, "w", encoding="utf-8").write(text)
    print("wrote docs/elements.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
