# Evidence model

The portable pattern is:

```text
immutable source
  -> isolated candidate
  -> operation
  -> observation
  -> integrity check
  -> deterministic judgement
  -> finding
  -> repair child
  -> compare
  -> perceptual judgement
  -> promotion/freeze
```

## Evidence layers

| Layer | Question | Typical evidence |
| --- | --- | --- |
| Source | Was the authored asset saved as intended? | DCC inspection, hierarchy, materials, bounds, origins, hashes |
| Import | Did the target engine accept that saved source? | Import report, scene-tree inspection, runtime roots |
| Automated runtime | Does a measurable contract hold? | Deterministic test, positive and negative cases, reset result |
| Real interaction | Does the real route produce the behaviour? | Input scenario, telemetry, reproducible runtime log |
| Perceptual | Does the result read as intended? | Motion/stills, reviewer, verdict, limitations |

An earlier layer does not prove a later one. A success message is not evidence
of the produced artifact. Technical measurements diagnose; they do not decide
taste or readability.

## Integrity and lineage

Observation paths must point inside the candidate workspace. Hashes or equivalent
integrity checks must be refreshed after any operation. A repair child must name
its real parent, failed source observation, hypothesis, and limited scope.

The close-out validator checks the machine-verifiable part of this contract;
the project adapter remains responsible for producing the observations.
