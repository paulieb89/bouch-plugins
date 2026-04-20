# Development — bouch-plugins marketplace

Maintainer notes. Not user-facing.

## Local test install (before pushing changes)

From within Claude Code, run:

```
/plugin marketplace add <your-local-clone-path>
/plugin install foundations@bouch-plugins
/reload-plugins
```

Or with the `--plugin-dir` flag for direct testing without adding the marketplace:

```bash
claude --plugin-dir <your-local-clone-path>/plugins/foundations
```

## Publishing checklist (first push or version bump)

1. Run validation: `python3 -m json.tool .claude-plugin/marketplace.json` and `plugins/foundations/.claude-plugin/plugin.json` — both must parse.
2. Verify every `plugins/foundations/skills/<name>/SKILL.md` has valid YAML frontmatter with `name` and `description` fields.
3. Pre-publish grep sweep for client/prospect names, personal identifiers, and internal paths:
   ```
   grep -rnE "Vice|Rockstar|GTA|Take-Two|Ahmed|Royston|SJB|Al Jazeera" .
   grep -rnE "paulboucherat|07711|articat1066" .
   grep -rnE "/home/[a-z]+/|company-pack/|research/" . | grep -v DEVELOPMENT.md
   ```
   All three should return zero hits (excluding this DEVELOPMENT.md).
4. Bump `version` in both `plugins/foundations/.claude-plugin/plugin.json` and the `plugins[0].version` field of `.claude-plugin/marketplace.json` (keep them in sync).
5. Commit. Push to `main` on `github.com:paulieb89/bouch-plugins`.
6. Verify from a fresh Claude Code session: `/plugin marketplace add paulieb89/bouch-plugins` then `/plugin install foundations@bouch-plugins`.

## Relationship to Anthropic's plugin-dev

Anthropic ships [plugin-dev](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev) — a comprehensive authoring toolkit. When working on `bouch-plugins`, install it:

```
/plugin marketplace add anthropics/claude-code
/plugin install plugin-dev
```

Useful agents: `plugin-validator`, `skill-reviewer`, `agent-creator`.
Useful command: `/plugin-dev:create-plugin` for scaffolding new plugins (use this when adding `property`, `legal`, `due-diligence` in weeks 2-4).

## Source of truth for skills

- SKILL.md source: `bouch-pages/company-pack/skills/<name>/SKILL.md` (BOUCH internal master, may include client examples and Paul-specific references).
- Public mirror: `github.com/paulieb89/bouch-mcp-skills` (standalone SKILL.md files, genericised).
- Plugin bundle: `bouch-plugins/plugins/foundations/skills/<name>/SKILL.md` (copy of the genericised mirror).

When updating a skill: edit the source in `company-pack/`, genericise, push to both `bouch-mcp-skills` (loose library) and `bouch-plugins` (bundled here). Two public copies of the same genericised content.
