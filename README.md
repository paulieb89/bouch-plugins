# BOUCH Plugins — Claude Code Plugin Marketplace

UK-specific Claude Code plugins for property investors, solicitors, small business owners, and project managers. Real SKILL.md format, MCP-backed where relevant, cross-checked against Anthropic's official agent skill standard.

**Marketplace name:** `bouch-plugins`
**Home:** https://github.com/paulieb89/bouch-plugins

---

## Quick install

```
/plugin marketplace add paulieb89/bouch-plugins
/plugin install foundations@bouch-plugins
/reload-plugins
```

Skills are namespaced as `/foundations:property-report`, `/foundations:humaniser`, etc. Run `/plugin` to see installed plugins and `/help` to see skills.

## Companion plugin

For plugin authoring workflows (scaffolding new plugins, validating manifests, building hooks), Anthropic's [plugin-dev](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev) plugin is recommended:

```
/plugin marketplace add anthropics/claude-code
/plugin install plugin-dev
```

This marketplace (`bouch-plugins`) focuses on UK-specific application plugins. `plugin-dev` focuses on authoring tools. They complement, they don't compete.

## What's in the marketplace

### property (v1.0.0)

7 skills backed by real Land Registry, Rightmove, and EPC data. The focused property investor toolkit.

```
/plugin install property@bouch-plugins
```

| Skill | What it does |
|-------|-------------|
| `property-report` | Full analysis from address or postcode: comps, EPC, yield, stamp duty, BUY/WATCH/PASS |
| `deal-screener` | Fast BUY/WATCH/PASS screen from a Rightmove URL or address |
| `investment-summary` | Client-ready investment brief from a Rightmove URL |
| `rightmove-investment-finder` | Search Rightmove for investments and rank by yield |
| `rightmove-quick-search` | Current listings + asking price vs recent sales comparison |
| `property-quick-comps` | Median price, transaction count, price per sqft for a postcode |
| `reduced-listings` | Motivated-seller finder — price cuts, time on market, restricted buyer pools |

MCP: `property-shared.fly.dev` (Land Registry, Rightmove, EPC register, SDLT). No API key.

---

### foundations (v1.0.0)

The BOUCH Skills Foundations pack. 10 curated skills demonstrating distinct patterns. Seven MCP-backed, three standalone:

| Skill | Pattern | What it does |
|-------|---------|--------------|
| `property-report` | Multi-MCP orchestration | Full UK property analysis from an address or postcode (requires the property MCP) |
| `pitch-research` | Multi-source research | Researches a UK company and drafts a cold outreach email backed by evidence (DD + web) |
| `cultural-intelligence` | Agent-driven dossier | Produces a cultural read on a creator, brand, or public figure (web + Reddit public JSON) |
| `mp-dig` | Parliamentary intel | Hansard + member interests + voting record on a given UK MP (uk-legal MCP) |
| `company-check` | Cross-register DD | Companies House + VAT + Charity + Gazette in one dossier (uk-due-diligence MCP) |
| `deal-screener` | Property screening | BTL / investment screen against a postcode or address (property MCP) |
| `legal-research` | Legal brief with citations | UK legal brief with statute and case-law citations (uk-legal MCP) |
| `workflow-auditor` | Structured scoring | Non-MCP. Finds where time actually gets lost in a repeated process |
| `humaniser` | Guardrail pattern | Non-MCP. Strips AI writing patterns from business text |
| `bouch-voice` | Style enforcement + skill chaining | Non-MCP. Applies BOUCH brand voice, internally calls humaniser first |

All skills follow the open [Agent Skills specification](https://agentskills.io/specification) and are portable across any compliant agent (35+ listed at [agentskills.io/clients](https://agentskills.io/clients)) — Claude Code, claude.ai, Codex, Cursor, Gemini CLI, GitHub Copilot, VS Code, Goose, Roo Code, and others. None of them are prompt templates dressed up as skills.

## Directory structure

```
bouch-plugins/
├── README.md
├── LICENSE
├── .claude-plugin/
│   └── marketplace.json
└── plugins/
    ├── property/                    ← UK Property Investor plugin
    │   ├── .claude-plugin/plugin.json
    │   ├── .mcp.json                ← property-shared.fly.dev
    │   ├── README.md
    │   └── skills/
    │       ├── property-report/     ← full gold structure (references/, assets/, scripts/)
    │       ├── deal-screener/       ← full gold structure
    │       ├── investment-summary/
    │       ├── rightmove-investment-finder/
    │       ├── rightmove-quick-search/
    │       ├── property-quick-comps/
    │       └── reduced-listings/
    └── foundations/                 ← 10-skill sampler across verticals
        ├── .claude-plugin/plugin.json
        ├── .mcp.json                ← Ledgerhall unified proxy
        ├── README.md
        └── skills/
            ├── bouch-voice/
            ├── company-check/
            ├── cultural-intelligence/
            ├── deal-screener/
            ├── humaniser/
            ├── legal-research/
            ├── mp-dig/
            ├── pitch-research/
            ├── property-report/
            └── workflow-auditor/
```

## Future plugins

Planned additions (not yet built):

| Plugin | Vertical | Status |
|--------|----------|--------|
| `property` | UK Property Investor OS — 7 property skills + `.mcp.json` for property-shared | **Live** |
| `legal` | UK Legal Research OS — 4 legal skills + `.mcp.json` for uk-legal-mcp + `/legal:*` slash commands | Planned, week 3 |
| `due-diligence` | UK Due Diligence OS — DD skills + `.mcp.json` for uk-due-diligence-mcp + `/dd:*` slash commands | Planned, week 4 |
| `p6` | UK P6 Schedule OS — 3 P6 skills + `.mcp.json` for pyp6xer-mcp | Future |
| `pinescript` | Pine Script Strategy OS — 2 Pine skills + `.mcp.json` for pinescript-mcp | Future |

Each will be free on the marketplace. The paid Gumroad products sell the **know-how layer**: installation walkthrough, playbook PDF, worked examples, decision trees, and maintainer support email. The infrastructure is free; the expertise is paid.

## License

MIT. See [LICENSE](./LICENSE). Plugins are free and open source. The BOUCH Gumroad products sell the guide, playbook, worked examples, and support, not the plugin files themselves.

## Maintainer

Paul Boucherat · paul@bouch.dev · bouch.dev · Nottingham, UK
