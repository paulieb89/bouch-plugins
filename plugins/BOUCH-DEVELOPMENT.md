# BOUCH development plugins

`bouch-supervision` helps a supervisor recover project context, choose whether to work directly or delegate, inspect outcomes and carry work across sessions. Its existing name is retained so installations can upgrade. `bouch-engineering` supplies a narrowly triggered evidence-assessment skill usable independently by coding agents. Neither depends on Runner, Notion, the Registry, Eve, an MCP server or the other plugin.

Both packages have a portable root `plugin.json` and a thin Claude manifest under `.claude-plugin/`. Supervision also retains its existing `.codex-plugin/plugin.json` compatibility overlay. Skills live once under each package's `skills/`. The existing `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json` list both packages using paths relative to the repository root. The local Codex catalogue is named `bouch-local`; the Claude catalogue is `bouch-plugins`.

## Install and validate

For local Codex use, add this repository as a marketplace if necessary, then install `bouch-supervision@bouch-local` or `bouch-engineering@bouch-local` with `codex plugin add`. The configured marketplace name must match the manifest. Restart or start a fresh session to pick up installed skills. For Claude Code, register this repository as a marketplace and install `bouch-engineering@bouch-plugins`, or test directly with `claude --plugin-dir <repository>/plugins/bouch-engineering`. `claude plugin validate <plugin-directory>` validates each Claude manifest and skill; validate the repository root separately for the Claude marketplace.

ChatGPT Work workspace import is a separate distribution step: its GitHub import must be given a repository/ref containing the committed marketplace and plugin files, with access to that repository. Local uncommitted files and a successful local Codex install do not establish workspace import or skill activation. See [workspace import documentation](https://learn.chatgpt.com/docs/enterprise/plugin-management) and [portable plugin packaging](https://developers.openai.com/plugins/build/plugins). No publishing or workspace import is implied by these instructions.

## Existing capability audit

The audited `bouch-agent-core` checkout included work newer than the catalogue's published `v0.2.4` pin. It remains independently usable and is not modified or copied here:

| Core skill | Assessment |
| --- | --- |
| `handoff-authoring` | Reusable for substantial handoffs; the supervisor includes only the minimal continuity it needs. Keep the detailed template canonical in Core. |
| `evidence-freeze` | Specialized preservation of verified baselines. Keep in Core; the Engineering skill addresses evaluating and attributing evidence before drawing conclusions, without requiring a freeze. |
| `environment-recon` | Useful when a capability surface has genuinely drifted; native discovery and a bounded check suffice for ordinary work. |
| `harness-extension` | Specialized when a real capability gap needs an extension; keep optional in Core. |
| `prime-authoring` | Useful when authoring an established project-specific prime; not needed for ordinary recovery. |
| `bouch-project-routing` | Historical BOUCH orientation with stronger Core/registry framing; do not impose it on these plugins. Revisit separately if its own users need current architectural language. |

The previous supervision skill's Runner and Notion directions are superseded by the current architecture. Generic implementation, review, testing and agent dispatch skills were not recreated. The evidence-assessment skill is a first experiment, not a claim that its additional value over both native agents has been proven; evaluate it against real cases before expanding the package.

## Initial verification — 2026-11-07

- Claude Code 2.1.319 validated each plugin and the Claude marketplace. Its public-directory checks additionally reported missing license and icon metadata; those are listing checks, not failures of local plugin validation. Public submission has not been attempted.
- Both plugins installed from this checkout into an isolated Claude configuration; `claude plugin details` listed their respective skills. A separate direct `--plugin-dir` Claude session invoked `bouch-engineering:engineering-evidence`; its native session recorded the expanded skill and response.
- Codex installed both plugins from `bouch-local`. A fresh Codex CLI session loaded the installed `engineering-evidence` skill and answered a missing-test-output scenario. This demonstrates loading and a narrow invocation, not comparative effectiveness.
- A fresh read-only Codex session used the installed supervision skill to recover this repository's dirty state and inspect the Claude session. It identified the outdated supervision Codex-overlay version; that mismatch was corrected after its observation. The Claude session was a skill invocation, not an implementation task, so this is not an end-to-end delegated implementation and review test.
- ChatGPT Work workspace import, installation and skill activation were not tested. The GitHub importer needs an accessible repository/ref containing these files and a workspace import. Do not infer Work capabilities or a successful import from local Codex tests.
