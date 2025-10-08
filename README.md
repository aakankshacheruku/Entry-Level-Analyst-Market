# Entry-Level-Analyst-Market

I'm rebuilding this project to understand how the entry-level data analyst job market actually looks — and why it has felt difficult lately. I'm combining public datasets from the Bureau of Labor Statistics (JOLTS + CPS) with a small sample of real job postings to measure demand, hiring, and “experience inflation” for early-career analysts. The pipeline pulls public data with Python, models it in DuckDB/SQL, and exports clean tables for dashboards.

## ✅ Project Progress — Entry-Level-Analyst-Market (as of October 7, 2025)

### Milestone Tracker

- [x] **Milestone 1 – Repository Setup & Initialization** *(September 27, 2025)*
- [x] **Milestone 2 – Data Pipeline Draft & Early ETL** *(September 28 – October 3, 2025)*
- [x] **Milestone 3 – Infrastructure & Validation Layer** *(October 4 – October 7, 2025)*
- [ ] **Milestone 4 – Environment Modernization & Resilient I/O** *(Upcoming)*
- [ ] **Milestone 5 – Metrics Standardization & Data Mart** *(Planned)*
- [ ] **Milestone 6 – Visualization & Dashboards** *(Planned)*
- [ ] **Milestone 7 – Documentation & Final Polish** *(Planned)*

---

**Progress Summary:**  
✅ 3 / 7 milestones complete — core ETL, infrastructure, and validation pipeline finished.  
📘 Documentation current through Milestone 3.  
🧩 Next focus: Python 3.11 upgrade and CSV fallback for validator (Milestone 4).

## Project Goal
To provide an honest, data-backed picture of how opportunities for new analysts are shifting — by combining hiring data, labor statistics, and live job requirements into one transparent dataset and dashboard.

## Data Ingestion (BLS JOLTS)
I pull seasonally adjusted level series for Job Openings (JTSJOL) and Hires (JTSHIL) from the Bureau of Labor Statistics API. This file lands in `data_raw/` and powers Hires per Opening (HPO), 12-Month Rolling Average, and Year-over-Year (YoY) trends.
