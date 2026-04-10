# Project Conventions

## Source of Truth

The `README.md` is the project manifest/spec -- the single source of truth for what the project is, what it contains, and how the pieces fit together. Keep it updated when adding components.

## Design Principles

- **KISS & YAGNI**: Never create something prematurely just because somebody *may* need it in the future -- not even if it's already scheduled. Wait until "first use" to nail down what is needed and implement it then.
- **Standard flat repo layout**: No reason to hide things from agents. Put everything into the standard location where you'd look (or even actually looked) for something first.
- **Aggressively clean/refactor**: Code and writing should be focused, maintainable, and high quality.

## Working Style

- Use subagents (sonnet) for implementing, testing, refactoring, analyzing, writing. No reason to wait for slower opus subagents or waste valuable context window yourself.
- Subagents can analyze a code file for you and fix minor things on the go that don't require your whole-picture-based decision.

## Escalation Policy

Escalate whenever something is too surprising to be straightforwardly dealt with:
- No API key in environment
- An assumption that Jörn made is wrong
- Anything that can affect other parts of the project in surprising ways

## Secrets

Never write the `FAL_KEY` or `CLOUDFLARE_API_TOKEN` secret envvars down anywhere in the repository.

## Quick Commands

```bash
python3 generate-image.py --help    # Generate missing card illustrations via FAL API
python3 render-card.py --help       # Render card definitions to print-ready PNGs
python3 print-layout.py --help      # Arrange rendered cards into print-ready PDF
```

## Deploying playtest-web

After changing files in `playtest-web/`, redeploy manually:

```bash
npx wrangler pages deploy playtest-web/ --project-name=treaty-playtest --branch=main
```

Production: https://treaty-playtest.pages.dev
