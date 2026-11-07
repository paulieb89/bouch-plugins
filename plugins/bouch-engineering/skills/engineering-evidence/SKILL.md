---
name: engineering-evidence
description: Assess the provenance and strength of engineering evidence across code, tests, running artifacts and agent sessions. Use when a result needs independent verification, evidence conflicts, or a change must be attributed across agents or a dirty working tree.
---

# Engineering evidence

Use this skill when the origin or meaning of evidence affects a real engineering decision. Apply only the checks relevant to the claim; ordinary development does not require an evidence ceremony.

1. State the claim and the exact target: repository and revision or working tree, artifact, environment and behavior. Identify any pre-existing changes before attributing work to an agent. A session summary or list of changed files alone does not establish authorship.
2. Inspect the actual artifact and the strongest practical source for the claim. Source code can show intended behavior; tests show the cases they exercised; a running system or rendered artifact can show behavior in that particular environment. None proves more than it observed. Check logs or native sessions for provenance when useful, without treating agent assertions as independent verification.
3. Check the test's scope, version and execution result. When a clean result is central and the instrument's sensitivity is uncertain, use an appropriate known positive or negative control if practical. Avoid modifying user data or production state for a control.
4. Reconcile conflicting or stale evidence by checking timestamps, revisions, inputs and environment. Prefer direct, relevant observations over summaries; explain unresolved conflicts rather than silently choosing one.
5. Report the observation, inference, evidence location and remaining limit separately. Preserve irreplaceable evidence in the project's established location when appropriate; do not require a new store, commit or tag merely to use this skill.
