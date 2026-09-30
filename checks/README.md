# Checks

The rules follow [`docs/claims-model.md`](../docs/claims-model.md). Run them locally with `python checks/audit.py`; the report is written to `build/audit/`. The workflow in `.github/workflows/audit.yml` runs them on every change to the registers and once a day.

Four checks need material the repository does not hold yet and are listed in each report as not yet checked: untyped later references and labels-to-manuscript mapping (both need the manuscript text), and composition-change and frozen-edition checks (both need history across runs).

Run on every change to `registers/`. **Errors** fail the check and are written to a standing error report, where each one stays open until a sync corrects it. **Review flags** are listed until someone resolves them.

| Check | Result | When |
| --- | --- | --- |
| Earned order | Error | A claim's `dependencies` (or `derives_from` relations) include a claim or element first earned in a later chapter |
| Untyped later reference | Review | A later concept appears in a claim with no declared dependency or relation |
| References resolve | Error | A cited claim, version, element, edition or hypothesis does not exist |
| No circular dependency | Error | Claims require one another in a cycle |
| Interpretation is not a premise | Error | A claim depends on one whose use is only representational |
| Composition matches dependencies | Error | A claim's `composition` differs from what its current `dependencies` derive |
| Composition change recorded | Error | A claim's composition changed without a matching correction or lineage-substitution event in its history |
| Superseded dependency | Review | A claim still depends on a superseded claim and has not been repointed to its successor or re-registered |
| Correction recorded | Review | A dependency was added to an existing claim as a correction |
| Labels unique per edition | Error | Two derivation appearances in one edition share a label |
| One derivation per claim | Error | A claim printed in an edition has no derivation appearance there, or more than one. Tests and forward pointers need exactly one statement appearance instead, and never a derivation |
| Only derivations are labelled | Error | A foreshadowing or restatement appearance carries a label of its own |
| Citations resolve | Error | A foreshadowing or restatement cites a label that is not a derivation in the same edition |
| Labels map to claims | Error | A labelled statement in the manuscript has no derivation appearance, or a derivation's label is not in the manuscript |
| Superseded claims stay out | Error | A superseded claim appears in a new edition without being marked historical |
| Status history is well formed | Error | A status change has no date, edition or reason |
| Use not classified | Review | A claim's use (constitutive, representational or diagnostic) is not yet recorded |
| Claim not mapped to elements | Review | A claim has no element concepts |
| Withholdings accounted for | Review | A withheld item names no destination and is not marked beyond the series or open |
| Released editions frozen | Error | The record or appearances of a released edition change |
| Sources resolve | Error | A cited source does not exist, or a role, kind or currency status is unknown. See [`docs/sources.md`](../docs/sources.md) |
| Status capped by evidence | Error | An entry's status is higher than its weakest premise source allows |
| Premise source checked | Review | A premise citation lacks what it is cited for, its locator, or the date and name of whoever checked it |
| Strongest objection recorded | Review | A premise source has no strongest objection recorded beside it |
| Premise source failed | Review | A premise source was retracted, failed to replicate or was superseded |
| Source due for recheck | Review | A source's currency has not been checked for a year |
| One line of evidence cited as several | Review | Two premise or support sources of one entry share a line of evidence |
| Exports are current | Error | `exports/` or `docs/elements.md` differs from what the registers generate. Regenerate with `python checks/export.py` and `python checks/elements_doc.py` |

## Daily audit

The checks also run once a day on a schedule, whether or not anything changed, finishing before 6:00 am Pacific. Each run updates one standing **Audit report** issue in this repository with:

- every open error and review flag, grouped by check;
- what is new since the previous run, and what was resolved;
- a count of claims still missing a derivation appearance.

A run that finds new errors or flags notifies the author through GitHub. At 6:00 am Pacific (America/Los_Angeles) each day, a scheduled Claude session reads the Audit report issue and sends the author a short plain-language summary. Both are set up together with the checks.

## Generated views

| Script | Writes | Source |
| --- | --- | --- |
| `checks/export.py` | `exports/` | All registers |
| `checks/elements_doc.py` | `docs/elements.md` | `registers/elements/elements.yaml` |
| `checks/lexicon_sync.py` | The Linking Lexicon page's data | `registers/elements/elements.yaml`. One way and additive: missing elements become nodes; existing nodes, formulas and notes on the page are never changed. Drift between the two is printed for review |
