# BOUCH Property Plugin

7 Claude skills for UK property investors. Real Land Registry sales data, Rightmove listings, EPC certificates, rental market analysis, and stamp duty — all from a single MCP connection.

**Install:**

```
/plugin marketplace add paulieb89/bouch-plugins
/plugin install property@bouch-plugins
/reload-plugins
```

Skills are available as `/property:property-report`, `/property:deal-screener`, etc.

---

## What's included

| Skill | What it does |
|-------|-------------|
| `property-report` | Full investment report from an address or postcode: comps, EPC, yield, stamp duty, rental analysis, BUY/WATCH/PASS verdict |
| `deal-screener` | Fast BUY/WATCH/PASS screen against underwriting criteria from a Rightmove URL or address |
| `investment-summary` | Client-ready investment brief from a Rightmove URL |
| `rightmove-investment-finder` | Search Rightmove for properties matching criteria and rank by yield |
| `rightmove-quick-search` | Current listings + how asking prices compare to recent sales |
| `property-quick-comps` | Median price, transaction count, price per sqft for a postcode |
| `reduced-listings` | Find motivated sellers — properties with price cuts, time on market, and restricted buyer pools |

## MCP server

This plugin connects to `property-shared.fly.dev`, a free hosted MCP server providing:

- **Land Registry** — comparable sales with EPC enrichment (price per sqft)
- **Rightmove** — live sale and rental listings, full listing detail
- **EPC register** — energy certificates, floor area, current and potential ratings
- **SDLT calculator** — stamp duty for any purchase price and buyer type

No API key required. Free.

## Data sources

All data comes from UK public registers and official APIs:

- Land Registry Price Paid Data
- Ministry of Housing EPC register
- Rightmove public listings
- HMRC stamp duty rules (2026 bands)

## Example queries

```
Analyse 47 Beeston Road, NG9 2EH — is it a good buy-to-let?
Screen this Rightmove listing: [URL]
What are 2-bed flats going for in NG1 3AL?
Find investment properties in Nottingham under £180k
What motivated sellers are there in DE22 right now?
```

## License

MIT. Free to use and modify. The BOUCH Gumroad products sell the playbook, worked examples, and support — not the plugin files.
