---
name: foreman-issue
description: Turns a plan agreed in a local session into a Foreman-ready GitHub issue (the shared Factory task form - Problem, Scope, Acceptance criteria, Out of scope) and files it, labelling it only when the user says so. Use when the user wants to hand work to Foreman or the factory, send a spec or plan as an issue, write a factory issue, or says "send it to Foreman".
---

# Foreman issue

Foreman builds only from the issue. Its stations start fresh with the issue text and a checkout of the repository's default branch. They never see this conversation, local files, uncommitted changes or unpushed branches.

## Before writing

1. Confirm the repository runs Foreman: its contract (`CLAUDE.md`/`AGENTS.md`) says so, or the user does. If not, stop and say so.
2. Settle every behaviour decision with the user now. Anything left open sends the run to the clarify lane, which costs a round trip.
3. One change, one repository. If the plan has independent parts, propose one issue per part in dependency order. File them together if the user likes, but each must merge before the next is labelled, or the pull requests conflict.
4. Anything the spec depends on must already be on the default branch. If it exists only locally (a design doc, a fixture, a decision record), get it merged first or put its content in the issue.

## Writing it

Title: `[Factory] ` then the change, in the imperative.

Body: the shared form's four sections, in this order, as `##` headings.

- **Problem**: what is wrong or missing, and how you know. Link the evidence: issues, PRs, CI runs, files at a commit.
- **Scope**: the files or area to change, and the behaviour chosen at every decision point. Name exact paths, functions, commands, inputs and expected outputs.
- **Acceptance criteria**: a `- [ ]` checklist. Each item is checked by a test or a command; write the command out where it helps. The reviewer judges the branch against this list, so it is the spec's teeth.
- **Out of scope**: what must not change, related work that belongs in another issue, and constraints such as "docs only" or "keep each file's existing style".

Rules:

- Self-contained: someone holding only the repository and this issue can build it.
- Point to repository paths and commits. Paste only short excerpts that are not in the repository.
- No secrets, tokens or private data. The issue text goes into model context and run traces.
- Don't ask for what Foreman can't do: merge, release, deploy, change another repository, or edit `.github/workflows/` (the push is refused unless the deployment allows workflow changes).
- Keep it tight. A narrow issue is cheap and done in minutes; a broad one costs several times more and often fails review after two rounds, which ends with findings on the issue and no PR.

## Filing

1. Show the user the full title and body. File only after they agree.
2. Write the body to a temporary file, then file it without the label:
   `gh issue create --repo <owner/repo> --title "<title>" --body-file <file>`
3. Report the issue URL.
4. Start the run only when the user says to. Labelling starts a paid, unattended run:
   `gh issue edit <n> --repo <owner/repo> --add-label factory`
   For a run the user wants to follow and steer, they comment `@<factory bot> <instruction>` on the issue instead (Bouch's deployments: `@eve-sf-app`).

## What comes back

- **Draft PR**: the user reads the diff and CI, then merges through the repository's own process.
- **Questions on the issue**: answer them on the issue, then remove the `factory` label and add it again. GitHub starts a run only when the label is applied.
- **Findings and no PR**: review failed twice. Narrow the issue, then relabel, or mention the bot with only the blocking points.

## Example

```markdown
[Factory] Note in the release skill that PR CI now gates merges

## Problem
#43 added `.github/workflows/ci.yml` and a ruleset that requires "Non-live tests" on `main` (PR #54). `.claude/skills/release/SKILL.md` still says the repo has no PR CI.

## Scope
- `.claude/skills/release/SKILL.md`, Gates bullet: say PRs merge once "Non-live tests" is green, as the ruleset enforces; the three local commands become an optional quicker check.
- Same file, step 6: open the PR, wait for "Non-live tests", then `gh pr merge --merge`.

## Acceptance criteria
- [ ] `grep -n "no PR CI" .claude/skills/release/SKILL.md` finds nothing
- [ ] Step 6 names the "Non-live tests" check and `gh pr merge --merge`
- [ ] `uv run pytest -m "not live" -q` still passes

## Out of scope
- No changes to workflows, hooks, tests or code. Docs only.
- Keep the file's existing hard-wrapped style.
```
