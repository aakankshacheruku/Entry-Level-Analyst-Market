# Roadmap

I'm rebuilding this project to understand the entry-level data analyst job market and why it feels difficult right now.

**Near-term scope**
1) Macro demand: BLS JOLTS (openings vs hires) → Hires per Opening (HPO), 12-month rolling, YoY.
2) Junior supply (planned): CPS cuts for recent grads / early career.
3) Requirements drift (planned): small, auditable sample of analyst postings (years of experience, degree, tools).

**This week**
- [x] Project scaffolding and README refresh
- [ ] JOLTS ingest script (raw → parquet)
- [ ] SQL model to compute HPO + rolling and YoY
- [ ] Makefile run target (etl → mart → export)
- [ ] Basic QA tests (shape, nulls, freshness)
- [ ] Processed CSV for Tableau + short usage notes
- [ ] CPS and postings plan docs
