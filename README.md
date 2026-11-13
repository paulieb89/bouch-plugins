# BOUCH Plugins — Plugin Marketplace

A plugin marketplace for BOUCH development plugins, game and character plugins, and UK-specific domain plugins (property, legal, small business, project management). Real SKILL.md format, MCP-backed where relevant, cross-checked against Anthropic's official agent skill standard.

**Marketplace name:** `bouch-plugins` (both the Claude and the OpenAI catalogue use this name)
**Home:** https://github.com/paulieb89/bouch-plugins

> 📘 **Free guide included.** The ~35-page [BOUCH Skills Guide](guide/) walks through writing your first skill, wiring MCP, and shipping a plugin. Markdown + PDF, CC BY-NC 4.0. Free to share and adapt with attribution.

---

## Current state of this checkout

This README describes the reconciled marketplace as intended for `main`. Both catalogues pin `bouch-agent-core` (Core) and `bouch-audio` to commits: the Claude entries pin release tags `v0.2.6` and `v0.2.0` plus their commit hashes, while the OpenAI entries pin the matching commit hashes only (Core `df1d28e27c4d466558c9c46b40b5d2ca168c96d2`, Audio `3d94024fad5d5f2a239864e42c3dc2727364d588`). Inspect any existing `bouch-plugins` source on your machine before adding or switching one; an older source may still carry an earlier catalogue.

Two catalogues live in this repository. They share a name and list the same nine plugins:

| Catalogue | File | Entries |
|-----------|------|---------|
| OpenAI / Codex | `.agents/plugins/marketplace.json` | Nine entries: seven local (`bouch-supervision`, `bouch-engineering`, `bouch-character-performance`, `foundations`, `property`, `legal-os`, `bouch-game-assets`), plus two externally sourced Git root entries, `bouch-agent-core` (Core) and `bouch-audio`, pinned by commit |
| Claude Code | `.claude-plugin/marketplace.json` | The same seven local plugins, plus the same two externally sourced entries, `bouch-agent-core` (Core) and `bouch-audio`, pinned by release tag plus commit hash in their own repositories (nine in total) |

Mentions of services below describe what a plugin is configured to use. They do not establish that any service is currently up or reachable.

---

## Quick install

Claude Code:

```
/plugin marketplace add paulieb89/bouch-plugins
/plugin install foundations@bouch-plugins
/reload-plugins
```

Codex CLI:

```
codex plugin marketplace add paulieb89/bouch-plugins
codex plugin add foundations@bouch-plugins
```

Adding without a ref follows the repository's default branch. To test an unmerged branch instead, append `#<branch>` (Claude Code) or `--ref <branch>` (Codex). See [plugins/BOUCH-DEVELOPMENT.md](plugins/BOUCH-DEVELOPMENT.md) for what has and has not been verified for Codex installs.

Skills are namespaced, e.g. `/foundations:property-report`, `/foundations:humaniser`. Run `/plugin` to see installed plugins and `/help` to see skills.

## Companion plugin

For plugin authoring workflows (scaffolding new plugins, validating manifests, building hooks), Anthropic's [plugin-dev](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev) plugin is recommended:

```
/plugin marketplace add anthropics/claude-code
/plugin install plugin-dev
```

This marketplace (`bouch-plugins`) provides BOUCH development, game and character plugins alongside UK-specific domain plugins. `plugin-dev` focuses on authoring tools. They complement, they don't compete.

## What's in the marketplace

Versions are as in the Claude manifest. `bouch-agent-core` and `bouch-audio` are pinned externally rather than versioned in this repository: the Claude entries by release tag and commit, the OpenAI entries by commit only.

| Plugin | Version | Catalogue | Area |
|--------|---------|-----------|------|
| `bouch-supervision` | 0.1.2 | OpenAI + Claude | Development supervision and continuity |
| `bouch-engineering` | 0.1.0 | OpenAI + Claude | Engineering evidence assessment |
| `bouch-character-performance` | 0.1.1 | OpenAI + Claude | Character design, voice and performance |
| `bouch-game-assets` | 0.1.1 | OpenAI + Claude | Game and 3D asset evidence loop |
| `legal-os` | 1.0.0 | OpenAI + Claude | UK legal research |
| `property` | 1.0.0 | OpenAI + Claude | UK property investment |
| `foundations` | 1.0.0 | OpenAI + Claude | Ten-skill sampler |
| `bouch-agent-core` | pin `v0.2.6` | OpenAI + Claude, external | Agent methodology (Core) |
| `bouch-audio` | pin `v0.2.0` | OpenAI + Claude, external | Audio production knowledge |

### bouch-supervision and bouch-engineering (BOUCH development plugins)

Two independent development plugins, each usable on its own:

| Plugin | What it is |
|--------|------------|
| `bouch-supervision` | Helps a supervisor recover project context, choose whether to work directly or delegate, inspect outcomes and carry work across sessions |
| `bouch-engineering` | A narrowly triggered evidence-assessment skill (`engineering-evidence`) for coding agents: assess the provenance and strength of evidence before drawing conclusions |

Neither requires `bouch-agent-core` (Core), the BOUCH Registry, Runner, Notion, Eve, an MCP server, or the other plugin. Core and the Registry are optional for both. Install either, both, or neither.

```
/plugin install bouch-supervision@bouch-plugins
/plugin install bouch-engineering@bouch-plugins
```

Each has a portable root `plugin.json` and a Claude manifest under `.claude-plugin/`; supervision also keeps a `.codex-plugin/plugin.json` overlay. The evidence-assessment skill is a first experiment; its added value over native agents has not been proven. See [plugins/BOUCH-DEVELOPMENT.md](plugins/BOUCH-DEVELOPMENT.md) for install, validation, the existing-capability audit and verification notes. A cloud copy of supervision was observed in ChatGPT Work and a user reported using it there; neither establishes GitHub sync or import of this repository.

---

### bouch-character-performance (v0.1.1)

Reusable guidance (the `character-performance` skill) for developing, voicing, animating and reviewing a character for visual or audio storytelling. It assumes no particular art style, voice provider, animation model or production stack. It has a root `plugin.json`, a Claude manifest and a Codex overlay, and ships no MCP configuration. No dependency on Core or the Registry is declared.

```
/plugin install bouch-character-performance@bouch-plugins
```

---

### bouch-game-assets (v0.1.1)

Evidence-led game and 3D asset production: the `game-asset-evidence-loop` skill, candidate lineage and bounded repair guidance, templates, and a project-independent close-out validator. Engine-agnostic; the consuming project owns its `/prime`, contract, adapters and runtime harness.

Its README recommends loading it alongside `bouch-agent-core`, which supplies the Registry MCP connection, so that is the setup to use when you want Registry access:

```
/plugin install bouch-agent-core@bouch-plugins
/plugin install bouch-game-assets@bouch-plugins
```

The plugin's validator tests (`python3 -m unittest discover -s tests -v`, from `plugins/bouch-game-assets`) cover the close-out validator. They do not establish the plugin's complete runtime requirements, so this README does not claim a proven hard dependency on Core or the Registry. The plugin README's own example installs both at `--scope user`; see [Checking a Bouch host](#checking-a-bouch-host) for how that interacts with the doctor.

---

### property (v1.0.0)

7 skills backed by Land Registry, Rightmove, and EPC data. The focused property investor toolkit.

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

MCP: the plugin's `.mcp.json` points at `property-shared.fly.dev` (Land Registry, Rightmove, EPC register, SDLT) with no API key configured. That is configuration; this README does not verify the service is currently available. The plugin has a Claude manifest but no Codex overlay, although the OpenAI catalogue lists it.

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

Its `.mcp.json` declares a `ledgerhall` server, and it has a Codex overlay. In a Codex test, enabling both `foundations` and `legal-os` produced a duplicate-`ledgerhall` warning (Codex skipped one declaration; both point at the same endpoint). That duplicate-name issue is unresolved. In a live Codex session with both plugins enabled, Codex logged the duplicate selection and then used the selected `ledgerhall` server for one read-only GOV.UK search, which succeeded; separately, direct `fastmcp` listed 76 tools on the live endpoint. A second, independent isolated Codex run with `legal-os` alone enabled also successfully called `ledgerhall` `gov_govuk_search` (bank holidays, count 1) and logged no duplicate warning. So the evidence is two single read-only search calls (one with both plugins enabled, one with `legal-os` alone) plus a tool listing. A `foundations`-alone run is not recorded, and none of this shows that every skill, other tools, or the other `ledgerhall` endpoints and skills work. See [plugins/BOUCH-DEVELOPMENT.md](plugins/BOUCH-DEVELOPMENT.md).

The skills use the open [Agent Skills specification](https://agentskills.io/specification) `SKILL.md` format, which many agents support (see [agentskills.io/clients](https://agentskills.io/clients)). The format is shared; runtime tool names and MCP integration differ by client and must be verified in the one you use. None of them are prompt templates dressed up as skills.

---

### legal-os (v1.0.0)

7 skills for UK legal research: legislation lookup, case law, HMRC/VAT guidance, parliamentary intent, MP research and full legal briefs with OSCOLA citations. Six skills are configured for the Ledgerhall MCP endpoint (pre-wired in the plugin's `.mcp.json`); `bailii-case-law` needs a locally running BAILII MCP server. In Codex, a read-only `gov_govuk_search` call through `ledgerhall` succeeded with `legal-os` enabled alone (no duplicate warning) and with `foundations` also enabled (see `foundations`); these are single calls, so per-skill activation and the other tools are unverified. See the [plugin README](plugins/legal-os/README.md).

```
/plugin install legal-os@bouch-plugins
```

---

### bouch-agent-core and bouch-audio (external sources, both catalogues)

These two appear in both catalogues as external Git sources, are optional, and are listed here for installation only. Neither is required by the development plugins above. Their Skills and knowledge live in their own repositories, and each marketplace entry pins a commit there (the Claude entries also pin the release tag; the OpenAI entries pin the matching commit hash only).

| Plugin | Canonical source | What it is |
|--------|------------------|------------|
| `bouch-agent-core` | [paulieb89/bouch-agent-core](https://github.com/paulieb89/bouch-agent-core) | Portable agent-development methodology: harness extension, environment recon, `/prime` authoring, evidence freeze |
| `bouch-audio` | [paulieb89/bouch-audio](https://github.com/paulieb89/bouch-audio) | Portable audio production knowledge: electronic production, mixing and mastering, audio verification |

**Historical doctor expectations, not universal requirements.** In the
Core/Registry architecture that `bouch-doctor` (optional, below) encodes,
`bouch-agent-core` is the host plugin and is expected user-wide, and
`bouch-audio` is treated as domain knowledge, reached through the Registry on
demand or enabled inside the project that needs it. The reasoning was that
installing domain knowledge user-wide makes every unrelated session carry it,
and the doctor reports that as a failure (`domain plugins installed
user-wide`). Neither scope is required of every user or project; follow your
own project's or user's authorisation and installation choices. The example
below shows that doctor-oriented arrangement.

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

**Codex.** The Codex catalogue lists both as external Git root sources pinned by commit. In a fresh isolated Codex environment, the nine-entry local marketplace was discovered and both external plugins installed successfully, as versions 0.2.5 (Core) and 0.2.0 (Audio). In a separate isolated skill probe, the Codex session explicitly read one Core skill (`handoff-authoring`) and one Audio skill (`audio-verification`); this does not show that every Core or Audio skill was exercised. That earlier probe had no Registry tool, so it says nothing about Registry access. A later isolated Codex candidate with a portable `mcp.json` called the live Registry successfully, and Claude called it via its existing manifest. ChatGPT Work Registry integration remains untested. A later isolated Codex installation fetched published Core v0.2.6 from GitHub using the updated marketplace entry and successfully queried the live Registry. A user's own environment may have a separately configured Registry; that is local state outside this repository.

Verified against Claude Code 2.1.278.

## Directory structure

Reflects this checkout. There are seven local plugin roots under `plugins/`; `bouch-agent-core` and `bouch-audio` live in their own repositories and have no directory here. Skill directories are listed by name only.

```
bouch-plugins/
├── README.md
├── AGENTS.md                         ← short agent guidance
├── DEVELOPMENT.md                    ← maintainer workflow
├── .agents/plugins/marketplace.json  ← OpenAI/Codex catalogue (9 entries)
├── .claude-plugin/marketplace.json   ← Claude catalogue (9 entries)
├── doctor/bouch-doctor               ← optional host-architecture check
├── doctor/bouch-act                  ← optional act layer: record → install plan → apply
├── guide/                            ← BOUCH Skills Guide (md + pdf, own LICENSE.txt)
└── plugins/
    ├── BOUCH-DEVELOPMENT.md          ← development plugins: install, audit, verification
    ├── bouch-supervision/
    │   ├── plugin.json
    │   ├── .claude-plugin/plugin.json
    │   ├── .codex-plugin/plugin.json
    │   └── skills/bouch-supervision/
    ├── bouch-engineering/
    │   ├── plugin.json
    │   ├── .claude-plugin/plugin.json
    │   └── skills/engineering-evidence/
    ├── bouch-character-performance/
    │   ├── plugin.json
    │   ├── .claude-plugin/plugin.json
    │   ├── .codex-plugin/plugin.json
    │   └── skills/character-performance/
    ├── bouch-game-assets/
    │   ├── plugin.json
    │   ├── .claude-plugin/plugin.json
    │   ├── LICENSE
    │   ├── README.md
    │   ├── assets/  evals/  references/  tests/  tools/
    │   └── skills/game-asset-evidence-loop/
    ├── legal-os/
    │   ├── .claude-plugin/plugin.json
    │   ├── .codex-plugin/plugin.json
    │   ├── .mcp.json                 ← Ledgerhall endpoint
    │   ├── LICENSE
    │   ├── README.md
    │   └── skills/                   ← 7: bailii-case-law, hmrc-tax-vat, legal-how-to,
    │                                    legal-research, legislation-lookup, mp-dig,
    │                                    policy-briefing
    ├── property/
    │   ├── .claude-plugin/plugin.json
    │   ├── .mcp.json                 ← property-shared.fly.dev
    │   ├── README.md
    │   └── skills/                   ← 7: deal-screener, investment-summary,
    │                                    property-quick-comps, property-report,
    │                                    reduced-listings, rightmove-investment-finder,
    │                                    rightmove-quick-search
    └── foundations/
        ├── .claude-plugin/plugin.json
        ├── .codex-plugin/plugin.json
        ├── .mcp.json                 ← Ledgerhall endpoint
        ├── LICENSE
        ├── README.md
        └── skills/                   ← 10: bouch-voice, company-check, cultural-intelligence,
                                         deal-screener, humaniser, legal-research, mp-dig,
                                         pitch-research, property-report, workflow-auditor
```

There is no repository-root `LICENSE` file in this checkout. Of the plugins, only `foundations`, `legal-os` and `bouch-game-assets` carry a `LICENSE`.

## Checking a Bouch host

**Relevant only if you use the Core/Registry architecture.** `doctor/bouch-doctor` is optional. It is not needed for the development plugins, `bouch-character-performance`, `legal-os`, `property` or `foundations`, nor for Codex installs. It matters for Claude Code hosts that use `bouch-agent-core` and the Bouch Registry, which is the setup the `bouch-game-assets` README recommends.

It is a read-only check: it writes, installs and repairs nothing, and exits 1 if any check fails. It verifies that a Claude Code host matches the Core/Registry runtime architecture: `bouch-agent-core` and the Bouch Registry MCP server are user-wide, domain knowledge is reached through the Registry on demand, and workbench capabilities stay in their projects. It reads expectations from the `bouch-plugins` marketplace as registered in Claude Code, the live Registry (`registry.bouch.dev`, so it needs network access and that service to be up) and Claude Code itself. The only local input is a checkout map at `~/.config/bouch/doctor.json`.

Behaviour to be aware of:

- It fails if the `bouch-plugins` marketplace is not registered or does not list `bouch-agent-core`.
- It treats every `bouch-plugins` plugin other than `bouch-agent-core` as domain knowledge, and reports an enabled **user-scope** install of one as `domain plugins installed user-wide`. By its logic that covers `bouch-supervision`, `bouch-engineering` and `bouch-game-assets` as well as `bouch-audio`. This encodes the Core/Registry model; it is not a statement that those plugins are defective. If you do not use that model, ignore the check or install project-scoped.
- `--full` starts fresh headless Claude sessions and uses API credit.

```
doctor/bouch-doctor          # local state and live Registry, a few seconds
doctor/bouch-doctor --full   # plus every declared entrypoint, remote source verification
                             # and fresh neutral/workbench session probes (uses API credit)
```

See `doctor/bouch-doctor --help` for the checkout map format.

## Acting on a discovered capability

`doctor/bouch-act` is the optional act layer next to `bouch-doctor`: doctor
checks what a host already has; `bouch-act` performs the record-to-installed
hop. It resolves a Registry record (or free-text query) to the concrete
install commands for each detected harness — Claude Code, Codex and Devin —
shows them, then applies on confirmation, backing up any config file it
edits. The remote Registry stays read-only; all acting is local.

```
doctor/bouch-act plan dev.bouch/reaper-mcp   # show the resolved steps, run nothing
doctor/bouch-act apply dev.bouch/reaper-mcp  # confirm, back up, run
doctor/bouch-act status                      # which records are installed where
```

Behaviour to be aware of:

- Only `bouch-agent-core` installs at user scope; domain plugins are planned
  at `local` scope so a `bouch-doctor` host stays green.
- For plugins the marketplace pin wins over a record's citation `ref`.
- On a Registry miss it also searches the official MCP Registry and GitHub
  and lists hits as **external (unvetted)** — shown for review only, never
  applied.
- It shares the `~/.config/bouch/doctor.json` checkout map with
  `bouch-doctor`, and writes new clones into it so doctor can check them.

## Releasing and updating plugins

Local plugins are versioned and released with this repository. External plugins (`bouch-agent-core`, `bouch-audio`) are released in their own repositories first; this repository then re-pins them in **both** catalogues: tag plus peeled commit in the Claude entry, commit only in the OpenAI entry. Neither catalogue is the sole pin. If a Core or Audio release is also distributed through a Bouch Registry record, that record is updated and verified separately in the Registry's repository; the marketplace does not do that for you.

Nothing pushes updates to consumers. Refreshing a marketplace re-reads the catalogue and may also refresh configured plugin files; verify the installed version and activation separately. A project's `enabledPlugins` cannot pin a version. A consumer that needs a qualified version should declare and check it itself (`audio-agent-workbench-v2` does this with a check script run from `/prime`) and should not silently fall back to a local copy if the dependency fails to resolve. `doctor/bouch-doctor --full` is an optional check that observes what fresh sessions actually receive, for hosts using the Core/Registry model; isolated install tests are another way.

The maintainer workflow (manifest rules, catalogue updates, validation, isolated testing, remote verification) is in [DEVELOPMENT.md](DEVELOPMENT.md). Prefer reading the running artifact, such as the remote tag or the live service, over the documentation that describes it.

## Future plugins

Vertical roadmap. `property` and `legal-os` already exist in this checkout; the remaining rows are planned additions (not yet built):

| Plugin | Vertical | Status |
|--------|----------|--------|
| `property` | UK Property Investor OS — 7 property skills + `.mcp.json` for property-shared | Present in this checkout |
| `legal-os` | UK Legal Research OS — 7 legal skills + `.mcp.json` for Ledgerhall | Present in this checkout |
| `due-diligence` | UK Due Diligence OS — DD skills + `.mcp.json` for uk-due-diligence-mcp + `/dd:*` slash commands | Planned, week 4 |
| `p6` | UK P6 Schedule OS — 3 P6 skills + `.mcp.json` for pyp6xer-mcp | Future |
| `pinescript` | Pine Script Strategy OS — 2 Pine skills + `.mcp.json` for pinescript-mcp | Future |

Pricing and licensing for planned plugins are not settled here. The paid Gumroad products sell the **know-how layer**: installation walkthrough, playbook PDF, worked examples, decision trees, and maintainer support email.

## License

MIT, as declared in the Claude marketplace entries for `foundations`, `property` and `legal-os`, and shipped as a `LICENSE` file in the `foundations`, `legal-os` and `bouch-game-assets` plugin directories. This checkout has no repository-root `LICENSE` file, and the other plugins do not carry one. The guide is CC BY-NC 4.0 (see `guide/LICENSE.txt`). No licence is declared here for the other plugins, so do not assume one. The BOUCH Gumroad products sell the guide, playbook, worked examples, and support, not the plugin files themselves.

## Maintainer

Paul Boucherat · paul@bouch.dev · bouch.dev · Nottingham, UK
