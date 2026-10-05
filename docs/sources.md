# Sources and the evidence standard

The book holds every source to one standard, whether it is a paper, a dataset, a proof or a run of the [Computational Companion](https://github.com/natanatan/Emergent-Existence-Companion). This page is the reference for the sources register and the checks that enforce the standard.

## Sources

Each source is one record, `registers/sources/EE-S-nnnn.yaml`. Like claim IDs, source IDs are permanent, opaque and never reused.

```yaml
id: EE-S-0001
citation: "Kemeny, J. G. and Snell, J. L. (1960). Finite Markov Chains. Van Nostrand."
url: null
kind: proof                 # measurement | replicated | proof | single-study | simulation | argument | opinion
line: kemeny-snell-1960     # line of evidence: sources from one group or one dataset share a line
method_visible: true        # can the method be inspected?
independent_check: none     # none | partial | replicated: has anyone checked it independently?
record: ""                  # the source's record on questions of this kind
interests: ""               # who gains if it is believed
strongest_objection: ""     # the best competing result or dissent, or the EE-S id of the source that makes it
degeneracy:                 # a specific alternative that would produce the same result, if one is known
  - alternative: ""         # e.g. "the result depends on the diffusion operator the model chooses"
    discriminator: ""       # the observable or calculation that would tell the readings apart
evidence:                   # for a measurement, replicated result or single study: what the experiment established
  conditions: ""            # what was controlled: preparation, geometry, couplings, detector
  observed: ""              # the outcome distribution actually reported
  uncertainty: ""           # uncertainty and significance, and the null model the significance is measured against
  rejected: []              # the null or competing models the result rules out
currency:
  status: current           # current | retracted | failed-replication | superseded
  last_checked: 2026-09-30
  by: null                  # the EE-S id of a superseding result, when there is one
companion: null             # for a Companion run: { module, spec_tag, commit, verdict }
```

The grade of a source comes from its `kind`, adjusted by four questions: whether its method is visible, whether anyone has checked it independently, what its record is on questions of this kind, and who gains if it is believed. No source is weighted up or down for being official.

## Citing a source

A claim or hypothesis lists the sources it relies on, each with a role:

```yaml
sources:
  - source: EE-S-0001
    role: lineage            # premise | support | lineage | foil
    cited_for: "The lumpability condition for Markov chains"
    level: effective        # observation | effective | mechanism | ontology
    locator: "§6.3"
    checked: { date: 2026-09-30, by: Natan Mallinger }
```

| Role | Meaning |
| --- | --- |
| `premise` | The claim fails if the source is wrong. Only premises carry the full checks |
| `support` | Adds weight, but the claim stands without it |
| `lineage` | Where the idea comes from |
| `foil` | A view the claim is set against |

### Level: what a citation is used for

A result and its interpretation are different things. A measurement or calculation reaches a claim through a model of what it tracks, an inference from that model, and only then an interpretation about what exists. The `level` field records how far along that chain a citation is used.

| Level | Meaning |
| --- | --- |
| `observation` | The measured or calculated result itself |
| `effective` | An effective description that fits the result within a stated regime |
| `mechanism` | A proposed mechanism that would produce the result |
| `ontology` | A claim about what underlying structure exists |

### Degeneracy

A source records a degeneracy only when a specific alternative is known: an omitted variable, a modeling choice or an unresolved factor that would produce the same result under a different reading, together with what would discriminate them. An alternative counts only when it predicts a discriminable difference; that an unknown variable *could* exist is not a degeneracy. An empty list (`degeneracy: []`) records that none is known; a source with no `degeneracy` field has not yet been asked, and a premise cited at `ontology` is flagged until it has.

### Evidence

An experiment establishes a conditional distribution, not a mechanism: under these conditions, these outcomes occur with these frequencies, within this uncertainty, against this null model. A significance measures incompatibility with that null model; it is not the probability that one interpretation is true. The `evidence` block records those four things (Natan's evidence note, questions 1 to 4), so that what a result discriminated stays separate from the vocabulary used to describe it ("path", "collapse", "virtual particle").

A result supports an ontology only as far as it discriminates it from the alternatives. When a known alternative (a `degeneracy`) reproduces the same distribution, the result supports what the two readings share, and a citation at `ontology` is flagged: cite it at `observation` or `effective`, or cite the experiment that tells them apart. The framework must reproduce the distributions; it inherits an interpretation only when an experiment has discriminated it.

## Rules and checks

| Rule | Check | Result |
| --- | --- | --- |
| Every citation resolves, with a known role and kind | Sources resolve | Error |
| **Status is capped by evidence.** An entry cannot stand higher than its weakest premise allows (table below) | Status capped by evidence | Error |
| A premise says what it is cited for, checked against the source, with the locator, the date and the checker | Premise source checked | Review |
| The strongest objection is recorded beside every premise source | Strongest objection recorded | Review |
| **Failure flags, it does not rewrite.** A premise that is retracted, fails to replicate or is superseded flags every entry resting on it for the author's review. The text changes only by the author's decision | Premise source failed | Review |
| Currency is checked on a schedule: every source at least once a year | Source due for recheck | Review |
| **A citation's level is capped by its source.** A premise cited at `mechanism` or `ontology` from a source of kind `simulation`, `argument` or `opinion` is flagged | Level exceeds source | Review |
| A premise cited at `ontology` names its source's degeneracies, or records that none is known | Degeneracy recorded | Review |
| An empirical premise (measurement, replicated, single-study) cited at `effective` or above records its conditions, observed distribution, uncertainty and rejected models | Experimental evidence recorded | Review |
| **Effect strength is not interpretation strength.** A premise cited at `ontology` whose source has a known degeneracy is flagged | Ontology not discriminated | Review |
| Independent lines, not citation counts. Two premise or support sources from one line are one line of evidence | One line of evidence cited as several | Review |

No scope inflation ("suggests" is not "shows", a simulation is not a measurement, a result in one regime is not a law) is a matter for review of `cited_for`; the checks cannot read it. The `level` field makes part of it checkable: the check "Level exceeds source" catches a simulation or argument cited for a claim about what exists.

## The cap

The highest status an entry may hold, given the weakest kind of source among its premises. **Proposed defaults, for the author to confirm.**

| Weakest premise | Highest status allowed |
| --- | --- |
| measurement, replicated result, proof | No cap from the source |
| single study, simulation, argument | Provisional |
| opinion | Speculative |

Retained and Derived rank above Provisional, which ranks above Speculative. Open, Deferred, Rejected and Superseded are never capped. A single unreplicated Companion run is a `simulation`, so it can move an entry to Provisional, not to Retained. A reimplementation that reaches the same verdict independently is a second line; with two lines the run's source can be recorded as `replicated`.

## Companion results

A Companion result reaches the book as one pull request that:

1. adds a source record for the run, `kind: simulation`, with `companion: { module, spec_tag, commit, verdict }`;
2. cites it from the hypothesis with the role it plays (usually `premise` for the entry the module tests);
3. adds a dated status event to the hypothesis, within the cap.
