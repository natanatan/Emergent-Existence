# Checks

> Pending: written once the claim notation is final.

Planned checks, run on every change to `registers/`:

| Check | Fails when |
| --- | --- |
| Earned order | A claim `requires` a claim, or uses a capability, that is first earned in a later chapter |
| References resolve | A cited claim or hypothesis ID does not exist |
| No circular dependency | Claims require one another in a cycle |
| Interpretation is not a premise | A claim `requires` one whose use is only representational |
| Withholdings are accounted for | A withheld item names no destination and is not marked beyond the series or open |
| Status history is well formed | A status change has no date, edition or reason |
