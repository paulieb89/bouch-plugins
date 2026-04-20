# BOUCH Skills Foundations — Claude Code Plugin

Ten curated Claude skills for UK professional work. Seven MCP-backed, three standalone. Demonstrates the range of patterns a real working skill library covers: multi-MCP orchestration, multi-source research, parliamentary intel, cross-register due diligence, property screening, legal briefs with citations, non-MCP guardrail patterns, and skill chaining.

## Install

```
/plugin marketplace add paulieb89/bouch-plugins
/plugin install foundations@bouch-plugins
/reload-plugins
```

Skills are namespaced. `/foundations:property-report`, `/foundations:humaniser`, etc. Run `/plugin` to confirm install, `/help` to browse loaded skills.

## MCP pre-wired

The plugin ships `.mcp.json` at its root. Install auto-configures the Ledgerhall MCP endpoint (`https://uk-business-mcp.fly.dev/mcp`, HTTP transport, no auth). Ledgerhall bundles all the UK data servers the MCP-backed skills depend on: Companies House, Charity Commission, Land Registry, The Gazette, HMRC, UK legislation, Hansard, GOV.UK, plus UK property data.

No manual setup needed. If you prefer to connect servers individually, disable the bundled `ledgerhall` entry and add `property-shared`, `uk-legal-mcp`, and `uk-due-diligence-mcp` directly.

## Skills

| Skill | Pattern | MCP |
|-------|---------|-----|
| `property-report` | Multi-MCP orchestration — full UK property analysis from address or postcode | Ledgerhall (property) |
| `pitch-research` | Multi-source research — researches a UK company and drafts evidence-backed cold outreach | Ledgerhall (DD) + web |
| `cultural-intelligence` | Agent-driven dossier on a creator, brand, or cultural figure | web + Reddit public JSON |
| `mp-dig` | Parliamentary intel — Hansard, member interests, voting record for any UK MP | Ledgerhall (uk-legal) |
| `company-check` | Cross-register DD — Companies House + VAT + Charity + Gazette in one dossier | Ledgerhall (uk-dd) |
| `deal-screener` | Property investment screen against a postcode or address | Ledgerhall (property) |
| `legal-research` | UK legal brief with statute and case-law citations | Ledgerhall (uk-legal) |
| `workflow-auditor` | Scoring framework — finds where time actually gets lost in a repeated process | none |
| `humaniser` | Guardrail pattern — strips AI writing tells from business text | none |
| `bouch-voice` | Skill chaining — applies BOUCH brand voice, invokes humaniser first | none |

The three non-MCP skills work immediately on install without any backend. The seven MCP-backed skills work immediately via the pre-wired Ledgerhall endpoint.

## Cross-client portability

All SKILL.md files in this plugin follow the open [Agent Skills specification](https://agentskills.io/specification). They are portable across any compliant agent, not just Claude Code. Compliant agents include Claude, Claude Code, OpenAI Codex, Cursor, Gemini CLI, GitHub Copilot, VS Code, Goose, OpenCode, Roo Code, and 25+ others listed at [agentskills.io/clients](https://agentskills.io/clients).

The plugin ships dual manifests so it installs as a native plugin on both Claude Code (`.claude-plugin/plugin.json`) and OpenAI Codex (`.codex-plugin/plugin.json`). Clients that don't support the plugin wrapper can read `skills/` directly.

For Claude.ai and Claude Desktop users who cannot install plugins, a markdown fallback zip with the same 10 skills ships alongside the paid Foundations Gumroad product.

## Authoring notes

If you want to build your own plugins, install Anthropic's [plugin-dev](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev) alongside this one:

```
/plugin marketplace add anthropics/claude-code
/plugin install plugin-dev
```

That plugin provides scaffolding, validation agents, and skill-authoring references.

## License

MIT. See [LICENSE](./LICENSE).

## Author

Paul Boucherat · paul@bouch.dev · [bouch.dev](https://bouch.dev) · Nottingham, UK

Part of the `paulieb89/bouch-plugins` marketplace. Paid Gumroad companion product ("BOUCH Skills Foundations — From Your First Skill to Your First Plugin", £39) available at [bouchmaster16.gumroad.com/l/skills-foundations](https://bouchmaster16.gumroad.com/l/skills-foundations). The plugin is free; the paid product is the teaching guide, worked examples, and playbooks on top of it.
