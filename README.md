# Job Market Navigator (Tableau-first)

A portfolio-ready project that measures labor-market conditions with a focus on **recent grads** and turns them into a **Tableau Public** dashboard.

## V1 deliverables
1. **Thermometer (Macro)** — Openings, Hires/Openings, Quits, Unemployment, LFPR (2015–present)  
2. **Early-Career Lens** — Unemployment for 20–24 and 25–34 vs Overall  
3. **Data Notes** — Seasonality, revisions, definitions, caveats

> v2 ideas: Remote/RTO overlays (SWAA), AI exposure explorer (SOC bins).

## Stack
- **Prep:** Python + DuckDB (optional) → CSVs in `data_mart/`  
- **Viz:** Tableau Public (connect to the CSVs)  
- **Code style:** small, auditable scripts → reproducible marts

## Quickstart
```bash
# create and activate a virtual env (example using uv)
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt

# run ETL to produce clean CSVs
python src/etl/jolts.py
python src/etl/cps_published.py

# (optional) build the mart with DuckDB (requires duckdb installed)
duckdb :memory: -c ".read src/sql/schema.sql" -c "COPY mart_macro TO 'data_mart/mart_macro.csv' (HEADER, DELIMITER ',');"
```

## Tableau
- Connect **`data_mart/mart_macro.csv`** (or directly `data_clean/*.csv` for v1).  
- Build two dashboards: **Thermometer** and **Early-Career Lens**.  
- Publish to Tableau Public and link back here.

## Caveats
- Public published CPS series are used (seasonally adjusted). Interpret **2015–present** trends with **revision cautions**.  
- Descriptive analysis only; no causal claims.

## Repo layout
```
job-market-navigator/
  data_raw/ data_clean/ data_mart/
  src/
    etl/               # Python scripts (BLS pulls -> clean CSVs)
    sql/               # DuckDB schema & marts
  notebooks/           # optional EDA
  tableau/             # workbook exports
  README.md
  requirements.txt
  Makefile
```
