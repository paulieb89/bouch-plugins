# BOUCH Plugins — Claude Code Plugin Marketplace

UK-specific Claude Code plugins for property investors, solicitors, small business owners, and project managers. Real SKILL.md format, MCP-backed where relevant, cross-checked against Anthropic's official agent skill standard.

**Marketplace name:** `bouch-plugins`
**Home:** https://github.com/paulieb89/bouch-plugins

> 📘 **Free guide included.** The ~35-page [BOUCH Skills Guide](guide/) walks through writing your first skill, wiring MCP, and shipping a plugin. Markdown + PDF, CC BY-NC 4.0. Free to share and adapt with attribution.

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

---

### bouch-agent-core and bouch-audio (external sources)

These two are listed here for installation only. Their Skills and knowledge live in their own repositories, and each marketplace entry pins a qualified release tag and commit there.

| Plugin | Canonical source | What it is |
|--------|------------------|------------|
| `bouch-agent-core` | [paulieb89/bouch-agent-core](https://github.com/paulieb89/bouch-agent-core) | Portable agent-development methodology: harness extension, environment recon, `/prime` authoring, evidence freeze |
| `bouch-audio` | [paulieb89/bouch-audio](https://github.com/paulieb89/bouch-audio) | Portable audio production knowledge: electronic production, mixing and mastering, audio verification |

**These two install at different scopes, and `bouch-doctor` enforces the
difference.** `bouch-agent-core` is the host plugin and belongs user-wide.
`bouch-audio` is domain knowledge, and domain knowledge is reached through
the Registry on demand or enabled inside the project that needs it —
installing it user-wide makes every unrelated session carry it, and the
doctor reports it as a failure (`domain plugins installed user-wide`).

```
# Host methodology — user-wide, once per machine
claude plugin install bouch-agent-core@bouch-plugins --scope user

# Domain knowledge — from inside the project that needs it
cd <your project>
claude plugin install bouch-audio@bouch-plugins --scope project
```

The project-scoped install writes `enabledPlugins` into that project's
`.claude/settings.json`, so the dependency is committed with the project
rather than held in your user configuration. Note that `enabledPlugins` is
a boolean map: it records *that* a project depends on a plugin, never which
release it was qualified against. A project that needs that guarantee
should declare the qualified version in its own contract and check it — see
`audio-agent-workbench-v2` for a worked example.

Verified against Claude Code 2.1.278.

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

## Checking a Bouch host

`doctor/bouch-doctor` is a read-only check that a Claude Code host matches the Bouch runtime architecture: bouch-agent-core and the Bouch Registry are user-wide, domain knowledge is reached through the Registry on demand, and workbench capabilities stay in their projects. It reads expectations from this marketplace, the live Registry and Claude Code itself. The only local input is a checkout map at `~/.config/bouch/doctor.json`.

```
doctor/bouch-doctor          # local state and live Registry, a few seconds
doctor/bouch-doctor --full   # plus every declared entrypoint, remote source verification
                             # and fresh neutral/workbench session probes (uses API credit)
```

See `doctor/bouch-doctor --help` for the checkout map format.

## Release and propagation lifecycle

How a local improvement becomes a release that existing consumers actually
receive. This is a description of what Web v0.2.0 and Audio v0.2.0 did, not
a proposal, and there is deliberately no automation: each stage is a
decision, and the platform already provides the mechanics.

The stages are distinct and it is worth not collapsing them — most of the
ways this goes wrong are a stage being skipped rather than done badly.

**1. Knowledge promotion — is this worth promoting at all?**
Decided in `agent-enumeration-lab` with the `promote-finding` skill, and
only for a finding already at VALIDATED. Its output is a proposal recorded
under `findings/promotion-candidates/`; it stops there and changes no
sibling repository. Promotion is not automatic, and a finding being
interesting is not promotion.

**2. Release qualification — does the package still earn its claims?**
In the package's own repository. Run its `scripts/validate-package.sh` and
its tests, and write what the release proves and does not prove into
`evidence/qualification.md`. The bar is the package's, not the consumer's:
bouch-audio v0.2.0 promoted one capability and left five demonstrated-but-
unqualified tools behind precisely because they had no seeded-fault checks.
Verify that previously qualified behaviour is unchanged rather than
assuming it — v0.2.0 compared old and new reports field by field.

**3. Publication — the release exists outside one machine.**
Commit, annotated tag, `git push` including the tag. Nothing downstream can
reference a release that is only local. Check what the remote actually has
(`git ls-remote --tags`); the commit to pin is the **peeled** tag
(`v0.2.0^{}`), not the tag object.

**4. Registry update — discovery points at the new release.**
Advance `source.ref` in the registry entry. The Registry is how an agent
finds a capability it does not already know about, so a stale ref means
fresh agents discover the old release. Convention: a record ref bump is a
minor release of the registry itself (`v0.3.0` carried web-workbench
v0.2.0; `v0.4.0` carried audio v0.2.0), published as a GitHub release so
the deployed service always corresponds to a release rather than a bare
`main`. Deployment happens in CI, not from a laptop. Verify live afterwards
— read an entrypoint back and check the commit it reports.

**5. Marketplace update — installation points at the new release.**
Advance `ref` **and** `sha` in `.claude-plugin/marketplace.json` and push.
This is the only place a plugin's version is pinned. Do not add a version
to the marketplace entry when the plugin carries its own `plugin.json`;
that version derives from the manifest.

**6. Consumer dependency update — existing consumers actually move.**
Nothing pushes. A consumer that is not updated keeps running the old
release, and the two patterns differ in whether that is visible:

| Pattern | Pin lives in | Update | Silent divergence? |
|---|---|---|---|
| Git submodule (web-workbench) | the consumer's own gitlink commit | check out the new tag, commit the submodule move | **No** — the pin is in the consumer's history |
| Marketplace plugin (bouch-audio) | this marketplace's `marketplace.json` | `claude plugin marketplace update bouch-plugins`, then `claude plugin install <plugin>@bouch-plugins --scope project` | **Yes, unless the consumer guards it** — `enabledPlugins` is a boolean map and cannot pin a version |

A plugin consumer that needs the guarantee must declare the qualified
version in its own contract and check it. `audio-agent-workbench-v2` does
this: CLAUDE.md states the qualified version, `tools/check-audio-dep.sh`
compares it with what Claude Code reports installed and enabled, and
`/prime` runs that on every session. Its policy on failure is the important
half — an unresolved dependency must not silently fall back to a local
copy, because that is how a superseded instrument keeps being used.

**7. Fresh-consumer verification — a new agent really gets it.**
The stage most easily skipped, because everything looks right on the
machine that did the work. `doctor/bouch-doctor` checks the host
architecture; `--full` additionally starts fresh headless sessions in a
neutral directory and in each workbench and compares their capability
surfaces, which is the only check here that observes what a new agent
actually receives rather than what configuration claims. It uses API
credit.

Whatever the stage, prefer reading the running artifact over the
documentation that describes it.

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
