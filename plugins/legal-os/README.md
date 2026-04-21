# BOUCH Legal OS — Claude Code Plugin

Seven Claude skills for UK legal research. Legislation search, case law, HMRC/VAT guidance, parliamentary intent (Pepper v Hart), MP research, and full legal briefs with OSCOLA citations. All backed by real data via the Ledgerhall MCP endpoint.

## Install

```
/plugin marketplace add paulieb89/bouch-plugins
/plugin install legal-os@bouch-plugins
/reload-plugins
```

Skills are namespaced. `/legal-os:legal-research`, `/legal-os:legislation-lookup`, etc. Run `/plugin` to confirm install, `/help` to browse loaded skills.

## MCP pre-wired

The plugin ships `.mcp.json` at its root. Install auto-configures the Ledgerhall endpoint (`https://uk-business-mcp.fly.dev/mcp`, HTTP transport, no auth). Ledgerhall covers UK legislation, case law, Hansard, HMRC guidance, GOV.UK, parliamentary debates and interests, and UK company data.

No manual setup needed. If you prefer individual servers, disable `ledgerhall` and connect `uk-legal-mcp` directly.

> **Bailii case law note:** The `bailii-case-law` skill requires a locally-running BAILII MCP server (STDIO transport). BAILII blocks cloud IPs so this skill cannot use Ledgerhall. Follow [bailii-mcp setup](https://github.com/paulieb89/bailii-mcp) to run it locally. The other six skills work immediately via Ledgerhall.

## Skills

| Skill | What it does | MCP |
|-------|-------------|-----|
| `legal-research` | Full UK legal brief — statute, case law, plain-English summary, OSCOLA citations | Ledgerhall (uk-legal) |
| `legal-how-to` | Lawyer's guide to the 5 core research workflows with example prompts and tool reference | Ledgerhall (uk-legal) |
| `legislation-lookup` | Search Acts + retrieve sections with in-force status | Ledgerhall (uk-legal) |
| `hmrc-tax-vat` | VAT rates, MTD status, HMRC guidance look-up | Ledgerhall (uk-legal) |
| `policy-briefing` | Parliamentary landscape, key MPs, reception assessment for a policy area | Ledgerhall (uk-legal) |
| `mp-dig` | Hansard debates, registered interests, and voting record for any UK MP | Ledgerhall (uk-legal) |
| `bailii-case-law` | UK case law search + full judgments from BAILII | bailii (local STDIO) |

## Reference material

Gold-standard skills ship with `references/` and `assets/` directories alongside the SKILL.md:

- `legislation-lookup/references/common-acts.md` — 50+ UK Acts with type/year/number codes for direct API calls, plus known API limitations
- `legislation-lookup/references/search-tips.md` — tips for `legislation_search`, point-in-time queries, commencement orders
- `legislation-lookup/assets/output-template.md` — standard output format for section lookups
- `hmrc-tax-vat/references/vat-reference.md` — VAT rates (standard/reduced/zero/exempt), registration thresholds, common supplies by category
- `hmrc-tax-vat/references/income-tax-reference.md` — 2025/26 tax bands, dividend rates, CGT, NI
- `hmrc-tax-vat/assets/example-queries.md` — copy-paste prompts for VAT, MTD, income tax, property, corporate tax
- `legal-how-to/references/tool-quick-ref.md` — all MCP tools with inputs/outputs, court codes
- `legal-how-to/references/oscola-quick-ref.md` — OSCOLA citation format for cases, legislation, Hansard
- `legal-how-to/assets/starter-prompts.md` — copy-paste prompts for common legal research tasks

## Known API limitations

Two known gaps documented in the reference material:

1. **Companies Act 2006** (`ukpga/2006/46`) — `legislation_get_toc` and `legislation_get_section` both return "Document is empty". The reference number is correct; the Act is not served by the legislation.gov.uk API. Use [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2006/46/contents) directly or search by keyword with `fulltext=true`.
2. **Domestic electricity VAT** — `hmrc_get_vat_rate` has no commodity entry for domestic fuel/power and returns 20% by default. The correct rate is 5% reduced, confirmed by [VAT Notice 701/19](https://www.gov.uk/guidance/vat-on-fuel-and-power-notice-70119). Use `hmrc_search_guidance` with "domestic fuel power VAT notice 701/19" instead.

## Cross-client portability

All SKILL.md files follow the open [Agent Skills specification](https://agentskills.io/specification). Portable across any compliant agent. The plugin ships dual manifests for Claude Code (`.claude-plugin/plugin.json`) and OpenAI Codex (`.codex-plugin/plugin.json`).

## License

MIT. See [LICENSE](./LICENSE).

## Author

Paul Boucherat · paul@bouch.dev · [bouch.dev](https://bouch.dev) · Nottingham, UK

Part of the `paulieb89/bouch-plugins` marketplace. Paid companion product ("BOUCH Legal OS", £49) available at [bouch.dev/products](https://bouch.dev/products/). The plugin is free; the paid product is the playbook, worked examples, and workflow guide on top of it.
