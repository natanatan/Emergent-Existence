# Architecture

Three repositories share one source of truth: the registers in this repository.

```
Emergent-Existence      public    manuscript + registers + checks
        │  exports/: claims, hypotheses, earned ladder
        ├──────────────► Computational Companion   public    runnable models that test claims by ID
        └──────────────► Emergent World            private   the interactive Expedition, gated on the earned ladder
```

## Rules

- **The registers are the source of truth.** The manuscript cites claims by ID. Other projects read `exports/` and never parse prose, so voice and style edits cannot break them.
- **Status lives only in the registers.** The prose does not state whether a claim is Retained, Provisional, Open and so on.
- **Model results flow back through the Hypothesis Register.** When a Companion run settles a question, the entry it bears on gets a new status history event that cites the run.
- **Manuscript order is editorial.** Folder names follow the current chapter order; claim IDs never do.
