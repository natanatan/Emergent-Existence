# Exports

Generated from `registers/` by `python checks/export.py`; never edited by hand. The audit fails if these files are out of date, so run the export after changing a register.

Other projects read these files and never the manuscript prose.

| File | Contents | Read by |
| --- | --- | --- |
| `manifest.json` | Schema version, editions, counts, and the map of merged (retired) claim IDs | Everyone |
| `claims.json` | Every active claim: kind, use, current status and wording, dependencies, relations, concepts, composition, appearances | Computational Companion, Emergent World |
| `hypotheses.json` | The Hypothesis Register: status, what would resolve each, where it is revisited | Computational Companion |
| `sources.json` | The sources register: what each source is, its kind, line of evidence, strongest objection and currency | Computational Companion |
| `companion-backlog.json` | The hypotheses a model run could settle | Computational Companion |
| `elements.json` | The element table | Emergent World, Linking Lexicon |
| `ladder.json` | The stages in order, the elements each earns, everything earned so far, and what each withholds | Emergent World |

A retired claim ID (merged into another) never appears in `claims.json`; `manifest.json` maps it to the claim that absorbed it.
