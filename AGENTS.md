# AGENTS.md

## Cursor Cloud specific instructions

### What this project is
"The Savings Game" is a single [oTree](https://otree.readthedocs.io/) behavioral-economics
experiment (Python). It is one product made up of several oTree apps (`savings_game`,
`filler`, `instructions`, `intervention_1..3`, `wisconsin`, `riskPreferences`,
`lossAversion`, `timePreferences`, `Numeracy`, `Finance`, `Inflation`, `session_results`).
Session configs are defined in `settings.py`. There is only one runtime service.

### Environment / dependencies
- Managed with `uv` (see `uv.lock` / `pyproject.toml`). The project targets Python 3.10
  (`environment.yml` pins 3.10.14); always run uv with `--python 3.10`. Dependencies live
  in `.venv` and are refreshed by the startup update script (`uv sync --python 3.10`).
- The `psycopg2` dependency is compiled from source and requires the system package
  `libpq-dev` (provides `pg_config`). This is only used for a Postgres production DB; local
  dev uses SQLite automatically.
- Run commands via `uv run ...` (e.g. `uv run otree devserver`).

### Running the app (dev)
- Start the dev server: `uv run otree devserver` → serves everything on
  `http://localhost:8000/` (redirects to `/demo`). SQLite (`db.sqlite3`) is created
  automatically; no other services (Postgres/Redis) are needed for local testing.
- Do NOT set `OTREE_PRODUCTION` for local dev. Note `.env.example` sets
  `OTREE_PRODUCTION = 1`, which turns OFF debug mode and expects Postgres — do not copy it
  to `.env` for local development. There is a hardcoded `SECRET_KEY` fallback in
  `settings.py`, so no secrets are required for dev.
- Test a flow end-to-end via the demo page: open `http://localhost:8000/demo`, pick a
  session config (e.g. "Numeracy Test" or "Complete Experiment"), open participant link P1,
  and click through. Standalone apps that need participant fields are prefixed by the
  `filler` app in their session config; `test_mode=True` in `SESSION_CONFIG_DEFAULTS` makes
  `filler` show a "blank page required during testing" — this is expected in dev.

### Lint / tests
- There is no lint tooling configured (no ruff/flake8/black/pre-commit) and no automated
  test suite (no `*/tests.py` oTree bot modules). `otree test <config>` will fail with
  `No module named '<app>.tests'` because none are defined. Validation is done by running
  the dev server and clicking through a demo session.

### Companion repo: `savings-game-analysis/`
- A second, separate repository (`github.com/o-nate/savings-game-analysis`, Python data
  analysis) is cloned into `savings-game-analysis/` and is `.gitignore`d by this repo — it
  has its own git history, so run `git` commands for it from inside that directory. It is
  NOT auto-updated on VM startup; `git pull` it manually there if you need the latest.
- It is also `uv`-managed (Python 3.10 via its own `.python-version`). Set up / refresh with
  `uv sync` run from `savings-game-analysis/` (this also does the editable install so
  `src`/`utils` imports resolve). The startup update script refreshes it automatically when
  the directory is present.
- Running the analysis scripts/tests end-to-end requires user-supplied inputs that are NOT
  in the repo: (1) experiment data files under `savings-game-analysis/data/` (that dir is
  gitignored/empty), and (2) a `.env` with JSON env vars `LABELS` and `EXP_1_LABELS`.
  Without them, importing modules like `src.preprocess` fails early (e.g. `LABELS` is
  `None`). The `tests/` files are plain scripts that run module-level `assert`s at import
  (not pytest/unittest) and depend on that data/config. The environment install itself is
  verified by importing the editable package + core deps (`pandas`, `numpy`, `statsmodels`,
  `duckdb`, `pingouin`, `seaborn`, `sklearn`).
