# Claims model

Canonical design, 29 September 2026. This is the reference for every register, check and export in this repository. The editor's version of it is the *Claims Design Spec*.

> **A claim is identified by the proposition it asserts and its inferential identity, not by where the book currently places it, how the book currently phrases it, or what the project currently thinks of it.**

## Five things kept separate

| Concept | Example | Identifies | Changes when |
| --- | --- | --- | --- |
| **Claim** | `EE-C-0137` | One proposition and its inferential identity | Never. A materially different assertion or inferential basis is a different claim |
| **Version** | `EE-C-0137@v3` | One wording or formalization of that proposition | The wording or notation improves without changing the assertion |
| **Edition** | `book-1/beta` | One release of one book's manuscript | A new release is cut. Editions freeze at release, not before |
| **Appearance** | Beta, `4.2` | One place where one edition prints one version of the claim, with its role (derivation, foreshadowing or restatement) | Per edition |
| **Element** | `Rd` (retained distinction) | One concept from the Linking Lexicon | The lexicon is revised |

## Claims

- **IDs are permanent, opaque and sequential.** `EE-C-nnnn`, never reused. The number records the order of registration and carries no meaning about position, importance or dependency.
- **An ID never encodes** volume, book, chapter, section, edition, stage, status, kind or label. All of these are mutable metadata.
- **IDs are assigned when a proposition first enters the canonical register,** not when it is first published. Book I claims are registered now, from the Beta audit. Claims found later get higher numbers even if they belong conceptually near Origin, and claims the Beta later discards keep their identities.

### When a claim becomes a new claim

A **materially different assertion**, or a **materially different inferential basis**, creates a new claim ID. The new claim `supersedes` the old one, and the old claim keeps its ID, history and dependencies, so citations of earlier editions still resolve.

A change to the dependency record is one of three things. Only the third creates a new ID.

| Kind of dependency change | Example | Result |
| --- | --- | --- |
| **Correction:** a dependency was always logically required but never declared | v3's formalization shows the claim needs `EE-C-0026` | Same ID. The dependency is added with a dated history event, and the build flags it for review |
| **Lineage substitution:** a dependency is superseded by a successor that plays the same inferential role | `EE-C-0024` is superseded by `EE-C-0301` | Same ID. The dependency is repointed to the successor with a dated history event. Allowed only when the dependent claim's own assertion and inferential role are unchanged |
| **Substantive re-grounding:** the claim now rests on a genuinely different premise or mechanism | the claim is re-derived from a different construction | **New ID**, superseding the old claim |

Until someone reviews it, the build lists every claim that still depends on a superseded claim.

### When two registrations turn out to be the same claim (merge)

The surviving claim lists the other ID in `aliases`, and takes over its appearances (each marked `merged_from`). The retired record stays in the register with `merged_into` pointing to the survivor and no appearances of its own. Its ID is never reused, and nothing may depend on it; references are repointed to the survivor.

## Versions

- A version holds the claim's wording and formal statement, the date it was introduced and the edition that first printed it.
- Earlier versions are never edited or deleted. An appearance in an old edition keeps pointing to the version it printed.
- Within an edition that has not been released, a claim's wording is edited in place: the current version is revised, not superseded. Versioning starts at release, so the voice pass and review edits of a draft do not create new versions.

## Editions

- One record per edition of one book: `id`, `volume`, `book`, `released`, `frozen`, `source_commit`.
- An edition in preparation has `released: null` and `frozen: false`; its text, appearances and wording may change.
- Release freezes it: `released` gets the date, `frozen` becomes true, and the record takes the fingerprint of the file sent and the source commit it was built from. Corrections after that go into the next edition.
- Book I Beta is in preparation. It is released when it is first shared with a peer for review.

## Appearances and labels

Every appearance has a **role**:

| Role | What it is | In print |
| --- | --- | --- |
| `derivation` | The claim's official formal derivation | Carries the label, e.g. Definition 4.2 |
| `foreshadowing` | An earlier mention pointing ahead to the derivation | No label. Cites the derivation's label forward, e.g. "(see 14.3)" |
| `restatement` | A later return to a claim already derived | No label. Cites the derivation's label back, e.g. "(4.2)" |
| `statement` | Where a test or a forward pointer is stated. These kinds are stated, never derived | No label in Book I Beta; mentions of it cite its section |

- **Tests and forward pointers are stated, not derived.** A claim of kind `test` (a diagnostic) or `forward_pointer` (a sketch of work deferred beyond the book) has exactly one `statement` appearance per edition and never a derivation. No derivation is to be invented for it.
- **Exactly one derivation appearance per claim per edition** for every other claim. The author assigns it. A claim without one is a hard error, which stays in the error report until a sync corrects it.
- **Only the derivation carries a label.** The label is a locator: the chapter and the order of derivations within it, for example `4.2`. The chapter counter counts derivation appearances only.
- **A type word may be printed with it** ("Definition 4.2"), but the type word is presentation, not identity.
- **Numbering resets in each edition.** The same claim can be `4.2` in the Beta and `5.1` in the first edition.
- **A label is unique within one edition.** Different editions may reuse a label for different claims.
- **Chapters are numbered continuously through a volume.** Book I is Chapters 1–14 and Book II begins at Chapter 15 (decided 30 September 2026), so a label is unique across a whole volume, not only within one book's edition. The two books are physical bindings; the numbering follows the argument.
- **Claim tags link the manuscript to the register.** In the source, each derivation or statement is preceded by an invisible tag, `<!-- EE-C-nnnn derivation -->` or `<!-- EE-C-nnnn statement -->`. Tags never print. The audit checks that every tag matches the register and every registered derivation or statement has its tag. A tag identifies the claim occurrence, not its printed position.
- **Use is never encoded in the label.** Whether a statement is a premise, a diagnostic or a representation is carried by the prose and recorded in the register.

```yaml
appearances:
  - { edition: book-1/beta, role: foreshadowing, cites: "4.2", chapter: 1, section: "1.9",  version: v2 }
  - { edition: book-1/beta, role: derivation, label: "4.2", type_word: Definition, chapter: 4, section: "4.9", version: v2 }
  - { edition: book-1/beta, role: restatement,   cites: "4.2", chapter: 9, section: "9.10", version: v2 }
  - { edition: book-1/ed1,  role: derivation, label: "5.1", type_word: Definition, chapter: 5, section: "5.2", version: v3 }
```

## Dependencies and relations

Dependencies are kept narrow. **`dependencies`** lists only the claims that must hold for this claim to hold: its constitutive premises. The earned-order check runs on these.

Every other link between claims goes in **`relations`**, with a type:

| Relation | Meaning | Earned-order check |
| --- | --- | --- |
| `derives_from` | Obtained from the other claim as a consequence | Treated like a dependency |
| `supersedes` | Replaces the other claim (the reverse link is generated) | None |
| `refines` | Sharpens the other claim without replacing it | None |
| `equivalent_to` | Asserts the same thing in a different form | None |
| `contrasts_with` | Is deliberately kept distinct from the other claim | None |
| `generalizes`, `specializes` | Is broader or narrower than the other claim | None |
| `foreshadows` | Points ahead to a claim earned later | Pass |
| `diagnoses`, `tests` | Uses the other claim as a check on a result | Pass |
| `represents` | Gives richer notation for a structure already earned (Formal Admissibility Rule) | Pass |

A later concept used with no declared dependency or relation is a **review flag**, never an error. Order in the book alone never fails a claim.

## Elements and composition

- **Elements are the concepts of the Linking Lexicon,** each with a two-letter code. They are grouped by **conceptual stage**, like the rows of a periodic table. The three foundations sit at the top: Origin (Ω), primitive Difference (𝔇) and admissible transformation (𝒰).
- **Stage is conceptual; chapter is editorial.** An element belongs to a stage, not permanently to a chapter. A chapter is the current manuscript location where that stage is developed. If Boundary becomes Chapter 5, `Bd` stays `Bd`. Stage assignment itself may be revised if the ontology is reorganized, and element codes never change when it is.
- **A claim's `composition` lists the elements it rests on constitutively,** for example `Rd·Ps`. It is derived from the claim's currently registered dependencies. It normally stays stable across wording versions, but it may change when the dependency record is corrected or carried forward to a successor. Such changes are recorded in the claim's history.
- Relations never enter the composition.
- The element table lives in `registers/elements/` and is shown in [`elements.md`](elements.md). The Linking Lexicon page is a view of it.

## Four graphs

| Graph | Question it answers | Built from |
| --- | --- | --- |
| **Claim graph** | Which propositions must hold for this proposition to hold? | `dependencies` and `relations` |
| **Element graph** | Which concepts are constitutively involved? | `composition` and the Lexicon's links |
| **Appearance graph** | Where does a reader encounter them? | `appearances` |
| **Edition graph** | Which formulation did a given release contain? | editions, versions and appearances |

The claim graph and the element graph overlap but are not the same graph, and the checks treat them separately.

## Status

- Status lives only in the register, as dated `status_history` events. The current status is the latest event.
- **The prose never prints status.** A proposition should not appear with different epistemic force because its register status changed between editions. The STRONG / OPEN / PROVISIONAL verdict markers are dropped; where uncertainty itself matters to the argument, the prose says so in words.
- Statuses are the Hypothesis Register's eight: Retained, Provisional, Derived, Open, Deferred, Rejected, Speculative, Superseded.

## Hypotheses

Hypotheses follow the same model. `EE-H-nnnn` is the identity, and the legacy `H-n` is kept as an alias. Their places in an edition are appearances.

## Sources

Claims and hypotheses cite the outside sources they rely on in a `sources` list, each with a role (premise, support, lineage or foil). An entry's status cannot stand higher than its weakest premise source allows. See [`sources.md`](sources.md).

## Complete claim record

```yaml
id: EE-C-0031
kind: criterion          # proposition | definition | criterion | test | ledger | representation | rule | forward_pointer
use: constitutive        # constitutive | representational | diagnostic
aliases: []
versions:
  v1: { text: "𝒫(Σ, r_ab) ≠ 𝒫(Σ, ∅)", introduced: 2026-09-29, edition: book-1/beta }
dependencies:
  - { claim: EE-C-0024, role: constitutive }
  - { claim: EE-C-0025, role: constitutive }
relations:
  - { type: contrasts_with, claim: EE-C-0023 }
composition: [Rd, Ps]    # derived from dependencies
appearances:
  - { edition: book-1/beta, role: derivation, label: "4.9", type_word: Criterion, chapter: 4, section: "4.17", version: v1 }
status_history:
  - { status: Provisional, date: 2026-09-29, edition: book-1/beta, reason: "Registered from Book I Beta" }
history:                 # corrections and lineage substitutions, with dates
  []
```

## Still open

- The printed label style: which type words are used, and how the locator is typeset.
