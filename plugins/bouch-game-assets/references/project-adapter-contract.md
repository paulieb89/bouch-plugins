# Project adapter contract

This package does not prescribe a universal engine or workbench API. A
consuming project should expose the smallest local commands or scripts needed
to produce these observations:

1. source structure and provenance;
2. target-engine import structure;
3. deterministic runtime checks;
4. real-input or reproducible interaction;
5. engine frames for every declared meaningful state;
6. integrity manifests and a close-out result.

Adapters must:

- operate on an isolated candidate, never the immutable source;
- keep scratch state and observations inside the declared candidate workspace;
- report the exact command and output path for each observation;
- test both the qualifying and non-qualifying boundary where applicable;
- leave the project in a resettable state;
- distinguish environment failure from a product or asset failure.

The adapter may use any native DCC, engine CLI, MCP surface, test runner, or
thin wrapper already provided by the project. Add infrastructure only after a
real production task demonstrates a missing capability.
