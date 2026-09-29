# Checks

> Pending: written once the claim notation is final.

Planned checks, run on every change to `registers/`:

| Check | Fails when |
| --- | --- |
| Earned order | A claim `requires` a claim, or uses a capability, that is first earned in a later chapter |
| References resolve | A cited claim, claim version or hypothesis ID does not exist |
| No circular dependency | Claims require one another in a cycle |
| Interpretation is not a premise | A claim `requires` one whose use is only representational |
| Withholdings are accounted for | A withheld item names no destination and is not marked beyond the series or open |
| Status history is well formed | A status change has no date, edition or reason |
| Labels are unique | Two claims share a printed label |
| One label per claim | A claim is printed under two different labels. A restatement cites the original label instead |
| Labels map to claims | A labelled statement in the manuscript has no claim, or a claim's label does not appear in the manuscript |
| Superseded claims stay out | A superseded claim is printed in a new edition without being marked historical |
| Released editions are frozen | The record of a released edition changes |
