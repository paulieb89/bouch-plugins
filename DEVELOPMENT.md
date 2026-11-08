# Development — bouch-plugins marketplace

Practical workflow for changing local plugins and for following a separately
released external plugin. Short agent guidance is in [AGENTS.md](AGENTS.md).
Be proportionate: a typo fix needs a JSON check; a version bump or new plugin
warrants an isolated install test.

## Layout

One repository, two host-specific catalogues, both named `bouch-plugins`. They
are separate files with different schemas; neither is generated from the other
and neither is the sole pin. Check both when a plugin is added, removed or
re-pinned.

| Host | Catalogue | Local entry | External entry |
|------|-----------|-------------|----------------|
| Claude Code | `.claude-plugin/marketplace.json` | `source: "./plugins/<name>"`, with `version` | `source: github`, `repo`, `ref` (tag), `sha` |
| OpenAI / Codex | `.agents/plugins/marketplace.json` | `source: local`, `path`, plus `policy`, `category` | `source: url`, `url`, `sha` (no tag) |

### Plugin manifests

Skills live once under `skills/`; manifests point at them.

| File | Purpose / where present |
|------|-------------------------|
| `plugin.json` | Portable manifest ([schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)): supervision, engineering, character-performance, game-assets |
| `.claude-plugin/plugin.json` | Claude manifest: every local plugin |
| `.codex-plugin/plugin.json` | Codex overlay (`skills`, `interface`, optional `mcpServers`): supervision, character-performance, foundations, legal-os |
| `.mcp.json` | MCP servers, referenced by `"mcpServers": "./.mcp.json"`: foundations, legal-os, property |

- Keep `name` and `version` aligned across a plugin's manifests and its Claude
  catalogue `version`. Descriptions and interface metadata may differ by host.
- Absence of a manifest is current state, not an error; add one only when the
  plugin should be offered on that host.
- Do not add `version` to an external catalogue entry; the pin is `ref` + `sha`.
- MCP config shows what a plugin is configured to use, not that the service is
  up. `foundations` and `legal-os` declare the same `ledgerhall` endpoint;
  Codex warns about the duplicate name when both are enabled.

### Source ownership

| Source | Content and version owned by | This repo records |
|--------|------------------------------|-------------------|
| Local `./plugins/<name>` | this repo | the files, and the Claude entry `version` |
| External (`bouch-agent-core`, `bouch-audio`) | their own repositories | Claude: `ref` + peeled `sha`; OpenAI: `sha` |

Never edit external plugin content here.

## Changing a local plugin

1. Inspect `git status` and the plugin's current manifests; preserve unrelated work.
2. Make the change, review the diff, and choose the target version.
3. Update every manifest carrying a version, and the Claude entry `version`.
4. Validate, and run an isolated install test if discovery, install or
   activation could be affected.
5. Commit and push as your authorisation and project policy allow, then verify
   the remote.

## Following an external release

1. Release in the plugin's own repository first, with its own validation.
2. Verify the remote tag and version:

   ```bash
   git ls-remote --tags https://github.com/paulieb89/<repo>.git 'vX.Y.Z*'
   git -C <plugin-checkout> show <sha>:plugin.json   # verify the published version
   ```

   Pin the **peeled** commit (the `vX.Y.Z^{}` line), not the tag object.
3. Update both catalogues as appropriate: Claude `ref` + `sha`; OpenAI `sha`.
4. If a Bouch Registry record also points at this release, change and deploy it
   in the Registry's repository, then read an entrypoint back from the live
   service and check the commit it reports. Not every plugin has a record; follow
   that repository's own release convention.
5. Validate, test in isolation, and update README pins.

## Validate

```bash
python3 - <<'PY'
import glob, json, sys
patterns = [".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json",
            "plugins/*/plugin.json", "plugins/*/.claude-plugin/plugin.json",
            "plugins/*/.codex-plugin/plugin.json", "plugins/*/.mcp.json"]
bad = 0
for pat in patterns:
    for f in sorted(glob.glob(pat)):
        try:
            json.load(open(f))
        except Exception as e:
            print(f"BAD {f}: {e}"); bad += 1
sys.exit(1 if bad else 0)
PY

claude plugin validate .                 # Claude marketplace
claude plugin validate plugins/<name>    # each changed plugin
python3 -m unittest discover -s plugins/bouch-game-assets/tests   # where a plugin has tests
```

Also check that versions agree (above), both catalogues list the same plugin
names with matching external SHAs, and each `SKILL.md` has `name` and
`description` frontmatter. For `foundations`, run the pre-publish sweep below.
Claude's public-directory checks may report missing license or icon metadata;
these are listing checks, not validation failures.

## Test in isolation

Use throwaway configuration so your own installation is not modified. Without
`CLAUDE_CONFIG_DIR` / `CODEX_HOME` these commands **do** change your real
configuration. Inspect any existing `bouch-plugins` source first; it may point
at an older catalogue or the earlier `bouch-local` identity. Authentication
inside a fresh config may be needed before a model session works.

```bash
(
export CLAUDE_CONFIG_DIR="$(mktemp -d)" CODEX_HOME="$(mktemp -d)"

claude plugin marketplace add "$PWD"
claude plugin install <name>@bouch-plugins
claude plugin details <name>@bouch-plugins        # or: claude --plugin-dir plugins/<name>

codex plugin marketplace add "$PWD"               # or paulieb89/bouch-plugins --ref <branch-or-tag>
codex plugin add <name>@bouch-plugins
)
```

Then start a fresh session and confirm what the change claims: discovery,
install, installed version, skill loading, and for MCP changes a read-only tool
call. Discovery and install do not show activation, and one loaded skill does
not show all skills work.

## After pushing

- **Marketplace refresh** re-reads the catalogue. Codex may also refresh
  configured plugin files, including disabled ones. Check the installed version
  and activation separately; install or update the plugin if needed.
- **ChatGPT Work import** is a separate workspace step needing an accessible
  repository/ref; see [plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management).
  A local install, an observed cloud version or a user report is not evidence of sync.
- `enabledPlugins` is a boolean map and cannot pin a version; consumers needing
  one must declare and check it.

Verify the remote with `git ls-remote origin` and a fresh add of the pushed ref.

## Optional tools

None is compulsory. `claude plugin validate`, `codex plugin ...` and Anthropic's
[plugin-dev](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev)
(`plugin-validator`, `skill-reviewer`) help when they fit. `doctor/bouch-doctor`
is an optional read-only host check (see the README), not a release gate.

## Foundations skill sources

This applies to existing `foundations` skills that originated in the BOUCH
company pack, not to every plugin. Historically: internal master
`bouch-pages/company-pack/skills/<name>/SKILL.md` (may contain client examples),
genericised public mirror `github.com/paulieb89/bouch-mcp-skills`, and the
bundle `plugins/foundations/skills/<name>/SKILL.md`. Verify a skill's actual
provenance first; some were authored here. Where the source exists, edit it,
genericise, and update mirror and bundle.

Before publishing `foundations` changes, expect no hits from:

```bash
grep -rnE "Vice|Rockstar|GTA|Take-Two|Ahmed|Royston|SJB|Al Jazeera" plugins/foundations
grep -rnE "paulboucherat|07711|articat1066" plugins/foundations
grep -rnE "/home/[a-z]+/|company-pack/|research/" plugins/foundations
```

## Official documentation

- Claude Code: [plugins](https://code.claude.com/docs/en/plugins),
  [plugin reference](https://code.claude.com/docs/en/plugins-reference),
  [marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- OpenAI / Codex: [Codex plugins](https://developers.openai.com/codex/plugins/build),
  [plugin packaging](https://developers.openai.com/plugins/build/plugins),
  [workspace management](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Agent Skills specification](https://agentskills.io/specification)

Where this file and those documents differ, the official documents win.
