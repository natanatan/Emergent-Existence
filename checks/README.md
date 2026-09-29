# Checks

> Pending: the code comes once the claims design is signed off. The rules follow [`docs/claims-model.md`](../docs/claims-model.md).

Run on every change to `registers/`. **Errors** block a change. **Review flags** are listed until someone resolves them.

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
| Labels unique per edition | Error | Two appearances in one edition share a label |
| Labels map to claims | Error | A labelled statement in the manuscript has no appearance, or an appearance's label is not in the manuscript |
| Superseded claims stay out | Error | A superseded claim appears in a new edition without being marked historical |
| Status history is well formed | Error | A status change has no date, edition or reason |
| Withholdings accounted for | Review | A withheld item names no destination and is not marked beyond the series or open |
| Released editions frozen | Error | The record or appearances of a released edition change |
