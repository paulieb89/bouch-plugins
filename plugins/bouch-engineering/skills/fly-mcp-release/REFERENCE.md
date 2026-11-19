# Reference

## Release contract template

Add this to each repo's `AGENTS.md`. Keep it to facts an agent can't get
faster from `release.yml`.

```md
## Release contract

- **Trigger:** publishing a GitHub Release runs `.github/workflows/release.yml`
  (tests → PyPI → Fly: <app names>). Pushing to `main` deploys <staging app | nothing>.
- **Version lives in:** `pyproject.toml`, `server.json` (×2), <any other spot,
  e.g. the server-card version in server.py>.
- **Bump:** `uv version X.Y.Z` (updates pyproject + uv.lock), then <other files>.
- **Validate:** `<command, e.g. uv run pytest -m "not live" -q | ./scripts/validate.sh>`
- **Notes:** generated from PR titles (`--generate-notes`); no CHANGELOG.
- **Verify in prod:** `https://<app>.fly.dev/.well-known/mcp/server-card.json`
  shows the version, `/health` returns 200, then <one real tool call>.
  <Drift script: `scripts/check-deploy-drift.sh`, if present.>
```

## Known traps

Each of these has cost a failed run or a wrong release in this fleet.

| Trap | What to do |
|---|---|
| `gh release create --target <short-sha>` returns `422 ... not a valid tag` | Pass a branch name or `$(git rev-parse origin/main)`. |
| Validation passed, then a later edit broke CI | Validate after the final edit, every time. |
| Version bumped in `pyproject.toml` only | Search for the old version string. Repos have 3–4 spots (server.json ×2, server-card code). |
| Bump tool didn't update `uv.lock`, and CI's `uv lock --check` fails | Use `uv version`, or run `uv lock` after the bump. |
| A fail-closed feature shipped before its secret existed | Set the secret first. Setting it restarts the machine, which is harmless. |
| Assumed only one app deploys | Read `release.yml`. Some repos deploy two apps from one release (for example property-shared → `propertydata` too). |
| PyPI looks stale after publishing | The JSON API is cached by a CDN. Check `https://pypi.org/simple/<pkg>/`, and use `uv … --refresh`, not `--refresh-package`. |
| `fly deploy` run "just to fix it quickly" | Never. It ships the working tree and skips PyPI. Release a new patch instead. |
| A tag was pushed but nothing happened | These workflows run on `release: published`, not on tags. Create the GitHub Release. |
| Health is green but the change isn't live | Make one real call against prod that exercises the change. |
