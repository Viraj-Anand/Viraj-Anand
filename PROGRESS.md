# Progress Report — Viraj-Anand repo

## Feature added
`data_quality.py` — a small, dependency-free data-quality checker suited to decision-analytics work.
- `data_quality_report(rows)` takes a list of row-dicts and returns:
  - `row_count`, `column_count`
  - `missing_counts` per column
  - `missing_fraction` per column
  - `duplicate_rows` count
- Raises `TypeError` for non-iterable input.

## Tests
`test_quality.py` — 6 pytest tests covering:
- basic report on a small dataset
- empty input
- duplicate-row detection
- all-missing column
- non-iterable input raises `TypeError`
- all columns missing

## Test results
`pytest` → 6 passed.

## Files
- `README.md` (pre-existing)
- `data_quality.py` (new)
- `test_quality.py` (new)
