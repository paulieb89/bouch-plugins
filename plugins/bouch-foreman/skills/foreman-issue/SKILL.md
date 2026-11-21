---
name: foreman-issue
description: Writes a plan agreed in a local session up as a Foreman-ready GitHub issue and files it with gh, adding the factory label only when the user says so. Use when the user wants to hand work to Foreman or the factory, file a factory issue, turn a spec or plan into a Foreman issue, or says "send it to Foreman", "file this for the factory" or "label it factory".
---

# Foreman issue

Foreman builds only from the issue. Its stations start fresh with the issue text and a checkout of the repository's default branch. They never see this conversation, local files, uncommitted changes or unpushed branches.

## Before writing

1. Confirm Foreman runs on this repository: the repository's `CLAUDE.md`/`AGENTS.md` or the user says so, and `gh label list --search factory` shows the label. If not, stop and say so.
2. Settle every behaviour decision with the user now; leave nothing for Foreman to choose.
3. One change, one repository. If the plan splits into parts, propose one issue per part. Label a part only after every part it depends on has merged; each run builds from the default branch.
4. Anything the spec depends on must be on this repository's default branch. If it exists only locally or elsewhere (a design doc, a fixture, a decision record, another repository's issue), merge it first or put its content in the issue.

## Writing it

Title: `[Factory] ` then the change, in the imperative.

Body: the shared form's four sections, in this order, as `###` headings.

- **Problem**: what is wrong or missing, and how you know. Link the evidence in this repository: issues, PRs, CI runs, files at a commit.
- **Scope**: the files or area to change, and the behaviour chosen at every decision point. Name exact paths, functions, commands, inputs and expected outputs.
- **Acceptance criteria**: a `- [ ]` checklist. Make each item checkable by a named test, a command (write it out), or a named place in a file.
- **Out of scope**: what must not change, related work that belongs in another issue, and constraints such as "docs only" or "keep each file's existing style".

Rules:

- Point to repository paths and commits; paste only short excerpts the repository doesn't hold.
- No secrets, tokens or private data. The issue text goes into model context and run traces.
- Don't ask for what Foreman can't do: merge, release, deploy, change another repository, or edit `.github/workflows/` (the push is refused unless the deployment allows workflow changes).
- Keep it narrow: one behaviour change, the fewest files that do it.

## Filing

1. Show the user the full title and body. File only after they agree.
2. Write the body to a temporary file outside the repository (`mktemp`), file it without the label, then delete the file:
   `gh issue create --repo <owner/repo> --title "<title>" --body-file <file>`
3. Report the issue URL.
4. Start a run only when the user says to. Both ways start a paid run, and both need the user's own rights on the repository:
   - Unattended: `gh issue edit <n> --repo <owner/repo> --add-label factory`. The labeller needs at least triage permission.
   - Attended, to follow and steer it: the user comments `@<factory bot> <instruction>` on the issue. Only owners, members and collaborators start a run this way. The bot is named in the repository's contract (`@eve-sf-app` on Bouch's deployments).

## What comes back

- **Draft PR**: the user reads the diff and CI, marks it ready, and merges through the repository's own process.
- **Questions on the issue**: answer them on the issue. For a labelled run, then remove the `factory` label and add it again; GitHub starts a run only when the label is applied. For a mention run, answer in a new mention.
- **Findings and no PR**: review still failed after two revision cycles. Narrow the issue, then relabel, or mention the bot with only the blocking points.
- **Duplicate note**: Foreman linked an existing issue and stopped. If they differ, say how on the issue and relabel.

## Example

Title: `[Factory] Note in the release skill that PR CI now gates merges`

```markdown
### Problem
#43 added `.github/workflows/ci.yml` and a ruleset that requires "Non-live tests" on `main` (PR #54). `.claude/skills/release/SKILL.md` still says the repo has no PR CI.

### Scope
- `.claude/skills/release/SKILL.md`, Gates bullet: say PRs merge once "Non-live tests" is green, as the ruleset enforces; the three local commands become an optional quicker check.
- Same file, step 6: open the PR, wait for "Non-live tests", then `gh pr merge --merge`.

### Acceptance criteria
- [ ] `grep -n "no PR CI" .claude/skills/release/SKILL.md` finds nothing
- [ ] Step 6 of `.claude/skills/release/SKILL.md` names the "Non-live tests" check and `gh pr merge --merge`
- [ ] `uv run pytest -m "not live" -q` still passes

### Out of scope
- No changes to workflows, hooks, tests or code. Docs only.
- Keep the file's existing hard-wrapped style.
```
