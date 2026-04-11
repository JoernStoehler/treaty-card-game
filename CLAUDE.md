# Project Conventions

## Source of Truth

The `README.md` is the project manifest/spec -- the single source of truth for what the project is, what it contains, and how the pieces fit together. Keep it updated when adding components.

## Current State

The game is being redesigned (v2). Key files:
- `design-v2.md` — game mechanics and rules
- `cards-v2.md` — card definitions with design notes
- `definitions.jsonl` — empty until we need to render/playtest; generate from `cards-v2.md`

Tooling (`render-card.py`, `playtest.py`, `playtest-web/`) is from v1 and needs updating before use. Don't update tooling until card content is finalized.

Legacy v1 content (`playtests/`, `handoffs/`) informed the redesign but describes old mechanics. Read for historical context only.

## Design Principles

- **KISS & YAGNI**: Never create something prematurely just because somebody *may* need it in the future -- not even if it's already scheduled. Wait until "first use" to nail down what is needed and implement it then.
- **Standard flat repo layout**: No reason to hide things from agents. Put everything into the standard location where you'd look (or even actually looked) for something first.
- **Aggressively clean/refactor**: Code and writing should be focused, maintainable, and high quality.

## Working Style

- **Do your own thinking, analysis, drafting, and writing.** You have the full context; subagents don't and can't catch up. Don't delegate understanding.
- Use subagents (sonnet) only for **reviewing finished work** — getting a second opinion on something you already wrote. Never for research, planning, or drafting.
- When you do use a subagent, **tell it exactly which files to read** — subagents that aren't given explicit file paths will skip reading and hallucinate from their training data.
- Don't make design decisions unilaterally. Document what the user decided, not what you think is best.

## Escalation Policy

Escalate whenever something is too surprising to be straightforwardly dealt with:
- No API key in environment
- An assumption that Jörn made is wrong
- Anything that can affect other parts of the project in surprising ways

## Secrets

Never write the `FAL_KEY` or `CLOUDFLARE_API_TOKEN` secret envvars down anywhere in the repository.

## Quick Commands (v1 tooling — not yet updated for v2)

```bash
python3 generate-image.py --help    # Generate missing card illustrations via FAL API
python3 render-card.py --help       # Render card definitions to print-ready PNGs
python3 print-layout.py --help      # Arrange rendered cards into print-ready PDF
```

## Deploying playtest-web (v1 — needs rewrite for v2)

```bash
npx wrangler pages deploy playtest-web/ --project-name=treaty-playtest --branch=main
```

Production: https://treaty-playtest.pages.dev
