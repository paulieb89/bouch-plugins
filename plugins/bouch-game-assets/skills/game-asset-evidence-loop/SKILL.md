---
name: game-asset-evidence-loop
description: "Use whenever a user builds, imports, repairs, verifies, playtests, or reviews a game-ready visual asset or 3D scene, including Blender/DCC assets, Godot or engine imports, modular kits, destruction, VFX, collision, pivots, or portfolio evidence. Separate source, import, runtime, real interaction, and perceptual truth; preserve immutable candidates and close out only on persisted evidence."
---

# Game Asset Evidence Loop

Use this procedure to make a game or 3D asset trustworthy in the target
project. A successful export, import, test, or render proves only that layer;
the produced runtime artifact and human judgement remain separate evidence.

## Establish the project contract

Before editing, read the project contract, visual language, import rules, and
existing Prime. Identify the engine, DCC, source asset, candidate workspace,
runtime owner, and existing validation routes. If a capability is unknown,
run bounded recon before inventing infrastructure.

Write down the acceptance contract:

- visual intent and gameplay distance;
- hierarchy, materials, origins, bounds, collision, mass, and pivot requirements;
- target-engine import and runtime behaviour;
- real interaction or reproducible scenario;
- meaningful states needing engine frames;
- exclusions and the required review owner.

Use the [candidate template](../../assets/asset-loop-record.template.yaml).

## Preserve candidate lineage

Never repair a source or failing candidate in place. Freeze the baseline,
create an isolated child candidate, record the failed observation, state the
hypothesis and scope, then rerun the required evidence layers. Keep all source,
execution, scratch, and observation paths inside the declared workspace.

Use a bounded repair budget; the default is three candidates. Repeated reruns
of an unchanged candidate do not consume a repair slot.

## Prove the layers in order

1. **Source:** inspect the real saved asset: hierarchy, names, origins,
   transforms, materials, meshes, bounds, collision, and provenance.
2. **Import:** import that saved candidate into the real target engine and
   inspect the resulting scene tree or runtime resource.
3. **Automated runtime:** run deterministic checks for measurable contracts,
   including qualifying and non-qualifying cases and reset behaviour.
4. **Real interaction:** exercise the input or scenario that matters. Measure
   values at the decision point; do not substitute post-contact values for
   pre-contact values or call a handler directly when the bug is in the live
   route.
5. **Perceptual review:** inspect gameplay distance and close range, preferably
   in motion. Record whether silhouette, causality, timing, scale, framing,
   effects, and material fit read as intended.

Project adapters own the commands and evidence files. Read the
[adapter contract](../../references/project-adapter-contract.md) before
creating one.

## Close out honestly

Use the [close-out manifest](../../assets/closeout-gate.template.json) and run
the bundled validator. A `provisional` candidate needs passed technical and
real-interaction evidence, engine frames for every meaningful state, and a
named review record. An `accepted` candidate additionally requires a named
human review with a pass verdict.

Persist selected observations, hashes, limitations, failed assumptions, and
human judgements. Keep raw logs linked rather than treating them as default
context. Do not claim a fresh pass when an environment blocked the check;
retain prior qualified evidence and record the limitation.

Read [the evidence model](../../references/evidence-model.md) when deciding
whether a result is sufficient or when a test and observed play disagree.
