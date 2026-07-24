# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Compares cricket fixture data from multiple sources for Welwyn Garden City Cricket Club (WGCCC) to ensure they stay in sync. The entry point `cricket/cricket.py` runs `compare_all()` which cross-checks Play Cricket, Google Calendar, Spond, and WPF Bookings against each other and prints discrepancies.

## Commands

```sh
# Install dependencies
pip install -r requirements.txt

# Run the fixture comparator (PYTHONPATH required due to bare imports in cricket/)
PYTHONPATH=cricket python3 cricket/cricket.py

# Run all tests (PYTHONPATH required — tests import directly from cricket/ modules)
PYTHONPATH=cricket python3 -m pytest

# Run a single test file
PYTHONPATH=cricket python3 -m pytest tests/reader/test_playcricket.py

# Run a single test by name
PYTHONPATH=cricket python3 -m pytest tests/reader/test_playcricket.py::test_name
```

## Architecture

### Data flow

```
data/ files → reader/ (parse to Fixture objects) → comparator/ (diff two lists) → printer/ (filter + print)
```

### Key types

- **`Fixture`** (`cricket/fixture.py`): Core data class. Fields: `wgc_team` (CricketTeam), `oppo` (str), `location`, `fixture_type`, `fixture_start_datetime`, `fixture_end_datetime`, `ground`. All datetimes are timezone-aware UTC internally, displayed in Europe/London.
- **`CricketTeam`** (`cricket/cricket_team.py`): Enum where each member holds `(team_name, team_fullname, division, host)`. Lookup methods: `get_value(name)`, `get_from_fullname()`, `get_from_division()`, `get_from_host()`.
- **`CompareFixture`** (`cricket/comparator/compare_fixture.py`): Looser equality wrapper around `Fixture` — equality is only `wgc_team + date + ground` (ignores time and opponent). Used for Spond and WPF comparisons where exact times aren't available.

### Data sources and their input formats

| Source | Directory | Format | Notes |
|--------|-----------|--------|-------|
| Play Cricket | `data/play-cricket/` | `.csv` | Exported from play-cricket.com; includes result column |
| Google Calendar | `data/google-calendar/` | `.ics` | Three calendars: Digswell Park, Welwyn Playing Fields, Away Fixtures. Ground is inferred from filename prefix. |
| Spond | `data/spond/` | `.csv` | Junior fixtures only; team identified via `host` field |
| WPF Bookings | `data/wpf/` | `.csv` | WPF home fixtures only |

### Comparison logic

- **Play Cricket vs Google Calendar**: uses full `Fixture.__eq__` (all fields must match), restricted to junior fixtures only
- **Play Cricket/Google Calendar vs Spond**: uses `CompareFixture.__eq__` (team + date + ground), filtered to future fixtures and non-senior types
- **Any vs WPF**: uses `CompareFixture.__eq__`, filtered to WPF-ground fixtures only

### Import note

The `cricket/` directory uses bare imports (e.g. `from fixture import Fixture`) rather than package-relative imports. `cricket/` must always be on `PYTHONPATH` — both for running the script and for running tests. Without it, all imports fail with `ModuleNotFoundError`.

### Adding a new data source

1. Add a new value to `SourceData` in `cricket/cricket_enums.py`
2. Create a reader in `cricket/reader/` following the pattern of existing readers (return a `list[Fixture]`)
3. Wire it into `parse_source_data()` in `cricket/cricket.py`
4. Add comparison logic in `cricket/comparator/compare_fixture_lists.py` if it needs non-standard equality
5. Add a call in `compare_all()` in `cricket/cricket.py`

### Adding a new team

Add a new member to `CricketTeam` in `cricket/cricket_team.py` with `(team_name, team_fullname, division, host)`. All four fields are used as lookup keys by different readers.
