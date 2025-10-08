# Entry-Level-Analyst-Market

I'm rebuilding this project to understand how the entry-level data analyst job market actually looks — and why it has felt difficult lately. I'm combining public datasets from the Bureau of Labor Statistics (JOLTS + CPS) with a small sample of real job postings to measure demand, hiring, and “experience inflation” for early-career analysts. The pipeline pulls public data with Python, models it in DuckDB/SQL, and exports clean tables for dashboards.

---

### ✅ Project Progress (as of October 7, 2025)

- [x] **Day 1 — Repository Setup & Initialization (Sept 27, 2025)**  
  Created `main-v2` branch · renamed repo · wrote new README · added `.env.example` + `.gitignore`.

- [x] **Day 2 — Data Pipeline Draft & Early ETL (Sept 28 – Oct 3, 2025)**  
  Implemented `bls_fetch.py` · validated BLS endpoints · wrote first Parquet outputs.

- [x] **Day 3 — Infrastructure & Validation Layer (Oct 4 – Oct 7, 2025)**  
  Built Makefile (`venv`, `deps`, `fetch`, `validate`) · added validator script · split dependencies · wrote Quickstart doc · verified 184-row dataset · tagged `day3-done`.

- [ ] **Day 4 — Environment Modernization & I/O Resilience (Upcoming)**  
  Upgrade to Python 3.11 · add CSV fallback · create `make sample` target.

---

## Project Goal
To provide an honest, data-backed picture of how opportunities for new analysts are shifting — by combining hiring data, labor statistics, and live job requirements into one transparent dataset and dashboard.

## Data Ingestion (BLS JOLTS)
I pull seasonally adjusted level series for Job Openings (JTSJOL) and Hires (JTSHIL) from the Bureau of Labor Statistics API. This file lands in `data_raw/` and powers Hires per Opening (HPO), 12-Month Rolling Average, and Year-over-Year (YoY) trends.
