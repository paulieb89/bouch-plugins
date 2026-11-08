# AGENTS.md — bouch-plugins

A marketplace repository for BOUCH plugins, with two host-specific catalogues
that share the name `bouch-plugins`:

- `.claude-plugin/marketplace.json` — Claude Code
- `.agents/plugins/marketplace.json` — OpenAI / Codex

Local plugins live under `plugins/<name>/`; `bouch-agent-core` and
`bouch-audio` are external and live in their own repositories. The workflow,
manifest conventions and verification steps are in
[DEVELOPMENT.md](DEVELOPMENT.md). Read it before changing manifests,
catalogue entries or versions. [README.md](README.md) describes the
marketplace; `plugins/BOUCH-DEVELOPMENT.md` records the development plugins
and what has been verified for Codex.

## Working here

- Work directly with your native tools and judgement. Delegation is optional;
  there is no mandatory approval or review gate for ordinary changes.
- Inspect `git status` and the current files first. Preserve existing user work
  and unrelated changes.
- The BOUCH Registry is optional discovery, not a prerequisite. There is no
  Runner dependency.
- Treat each plugin's manifests as one set: keep `name` and `version` aligned
  across them. Descriptions and interface metadata may differ by host. Where a
  plugin appears in both catalogues, check that its identity and any pin agree.
- Do not edit an external plugin's content here. Its source repository owns it;
  this repository only pins a release.
- Follow the user's existing authorisation and project policy for git and
  release actions; account for the distinct effects of each action.
- Distinguish what you verified (command output, a fresh install) from what you
  inferred. Do not claim a Work sync, Registry deployment or skill activation
  from local tests.
