# Checks

> Pending: the code comes once the claims design is signed off. The rules follow [`docs/claims-model.md`](../docs/claims-model.md).

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
| One derivation per claim | Error | A claim printed in an edition has no derivation appearance there, or has more than one |
| Only derivations are labelled | Error | A foreshadowing or restatement appearance carries a label of its own |
| Citations resolve | Error | A foreshadowing or restatement cites a label that is not a derivation in the same edition |
| Labels map to claims | Error | A labelled statement in the manuscript has no derivation appearance, or a derivation's label is not in the manuscript |
| Superseded claims stay out | Error | A superseded claim appears in a new edition without being marked historical |
| Status history is well formed | Error | A status change has no date, edition or reason |
| Withholdings accounted for | Review | A withheld item names no destination and is not marked beyond the series or open |
| Released editions frozen | Error | The record or appearances of a released edition change |

## Daily audit

The checks also run once a day on a schedule, whether or not anything changed. Each run updates one standing **Audit report** issue in this repository with:

- every open error and review flag, grouped by check;
- what is new since the previous run, and what was resolved;
- a count of claims still missing a derivation appearance.

A run that finds new errors or flags notifies the author. The workflow is written with the checks.
