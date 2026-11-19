---
name: fly-mcp-release
description: Cut, ship and verify a release of a Python MCP server deployed to Fly.io, where publishing a GitHub Release triggers release.yml (tests, PyPI, Fly deploy). Use when asked to release, cut a release, bump the version, ship or deploy one of these servers (the mcpfleet repos and similar), or to check that a release actually reached production.
---

# Fly MCP release

The repo's `release.yml` is the machinery and the authority. This skill is the
procedure around it. Never run `fly deploy` by hand: it ships the working
directory, skips PyPI, and leaves prod, PyPI and the tag disagreeing.

## Before starting

1. Read the repo's **Release contract** section in `AGENTS.md` (or `CLAUDE.md`).
   If there isn't one, work it out from `release.yml`, `pyproject.toml` and
   `server.json`, then propose adding one. Template: [REFERENCE.md](REFERENCE.md).
2. Read `release.yml`: what it checks, which apps it deploys, what secrets it
   needs.

## Workflow

- [ ] **Preflight.** `git status` is clean, you're on `main`, `git pull --ff-only`
      succeeds, and CI on `main` is green.
- [ ] **What's shipping.** Run `git log $(git describe --tags --abbrev=0)..origin/main --oneline`.
      Read each merged PR (`gh pr view N`). If nothing user-facing changed,
      say so and stop.
- [ ] **Choose the bump.** Patch for fixes. Minor for features or breaking
      changes, unless the contract says otherwise.
- [ ] **Prep branch** `release/vX.Y.Z`. Bump **every** version file the
      contract lists. Use `uv version X.Y.Z` where `pyproject.toml` is the
      source; it also updates `uv.lock`. Re-lock if the bump tool doesn't.
      Search for the old version string to catch any spot you missed.
- [ ] **Validate after the last edit**, using the contract's command. A check
      run before your final edit doesn't count.
- [ ] **PR** titled `release: vX.Y.Z — <summary>`. Wait for CI. Ask before
      merging, then squash-merge.
- [ ] **Pre-release.** Set any secret or config the release needs first
      (`fly secrets list -a <app>`). A feature that refuses all requests when
      it isn't configured must be configured before the deploy.
- [ ] **Confirm with the user, then publish:**
      ```bash
      gh release create vX.Y.Z --target "$(git rev-parse origin/main)" \
        --generate-notes --title "vX.Y.Z — <summary>" \
        --notes "<breaking changes or actions needed, if any>"
      ```
      `--target` must be a branch or the **full** SHA; a short SHA fails with
      a 422 error. `--notes` is added above the generated notes, so use it
      only for what PR titles can't say. Let `gh` create the tag.
- [ ] **Watch:** `gh run watch <run-id> --exit-status`. If it fails, fix the
      cause and publish a new patch release. Don't re-run steps by hand.
- [ ] **Verify production** with the contract's checks. Always include:
      - the version in the server card or `serverInfo`;
      - `/health`;
      - the drift script, if the repo has one;
      - **one live call that exercises what the release changed**.
      Green CI isn't proof; observable behaviour is.
- [ ] **Report** the version, the PR, the release URL, verification results,
      and anything left open.

## Release notes come from git

Repos following this standard keep no `CHANGELOG.md`. The release notes are
the merged PR titles, so:
- write PR titles as Conventional Commits (`feat:`, `fix:`, `docs:`, `release:`);
- put the reason for a change in the PR body;
- mark breaking changes `BREAKING:` in the PR body, and repeat them in
  `--notes`.

A repo that still keeps a CHANGELOG, or tests one, follows its contract until
that's removed.

## Out of scope

Libraries with no Fly app (for example `mcpfleet-obs`, which publishes with
`twine`), and Vercel or eve projects. Follow their own repo guidance.

Known traps and the contract template: [REFERENCE.md](REFERENCE.md).
