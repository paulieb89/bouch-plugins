# bouch-game-assets

Portable Bouch guidance and tooling for game-ready visual assets and 3D
projects. This package carries the evidence loop and close-out gate, not a
universal engine harness.

## What it provides

- the `game-asset-evidence-loop` Skill;
- a source/import/runtime/real-interaction/perceptual evidence model;
- immutable candidate lineage and bounded repair guidance;
- a project-independent close-out validator;
- templates for candidate records, close-out manifests, and review reports.

## What the consuming project provides

Each project owns its `/prime`, visual/gameplay contract, source and candidate
layout, DCC/engine adapter, deterministic fixtures, real-input scenario, and
runtime-specific commands. The package deliberately does not define a
universal candidate schema or workbench CLI.

## Install

Load this package as a Claude plugin alongside `bouch-agent-core`:

```text
claude plugin install bouch-agent-core@bouch-plugins --scope user
claude plugin install bouch-game-assets@bouch-plugins --scope user
```

`bouch-agent-core` supplies the Registry MCP connection. Registry discovery is
read-only; it does not install project adapters or carry live project state.

## Validate

```text
python3 -m unittest discover -s tests -v
python3 tools/validate_closeout_gate.py <candidate>/closeout-gate.json --workspace <candidate>
```
