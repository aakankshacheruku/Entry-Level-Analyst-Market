# Job Market Navigator

This project explores U.S. labor market conditions, with a focus on recent graduates navigating today’s job market. I built Python ETL scripts to pull and clean JOLTS and CPS data from the Bureau of Labor Statistics, then designed Tableau dashboards to visualize key indicators like openings, hires, unemployment, and conversion efficiency.

---

## Dashboards (Tableau Public)

- **Thermometer** — Macro view of labor market tightness and conversion  
  (Job Openings, Hires per Opening, Quits Rate, Unemployment Rate, LFPR)

- **Early-Career Lens** — Unemployment trends for ages 20–24 and 25–34 compared to the overall workforce

*(links coming soon as dashboards are published)*

---

## Data Pipeline

- **ETL scripts (`/src/etl`)**: Python code that pulls JOLTS and CPS series from the BLS API and saves them as clean CSVs (`/data_clean/`).  
- **DuckDB schema (`/src/sql`)**: Builds a consolidated mart (`/data_mart/mart_macro.csv`) with derived KPIs such as Hires per Opening and rolling volatility.  
- **Outputs**: These CSVs feed directly into Tableau dashboards.

---

## Repo Highlights

- `/src/etl` → Python ETL for JOLTS and CPS data  
- `/src/sql` → DuckDB schema & KPI definitions  
- `/data_clean`, `/data_mart` → Clean and mart CSVs for Tableau  
- `/docs` → Experiment logs and notes  
- `/tableau` → Workbook exports

---

## Roadmap

Planned improvements and extensions include:
- Adding remote vs. return-to-office overlays
- Exploring AI-exposure by SOC codes
- Building state-level or regional breakdowns for youth unemployment
- Automating monthly refreshes

---

## Notes

- Data are from publicly available, seasonally adjusted BLS series.  
- Revisions can affect the most recent months; interpretation should account for

cat > README.md << 'EOF'
# Job Market Navigator

This project explores U.S. labor market conditions, with a focus on recent graduates navigating today’s job market. I built Python ETL scripts to pull and clean JOLTS and CPS data from the Bureau of Labor Statistics, then designed Tableau dashboards to visualize key indicators like openings, hires, unemployment, and conversion efficiency.

---

## Dashboards (Tableau Public)

- **Thermometer** — Macro view of labor market tightness and conversion  
  (Job Openings, Hires per Opening, Quits Rate, Unemployment Rate, LFPR)

- **Early-Career Lens** — Unemployment trends for ages 20–24 and 25–34 compared to the overall workforce

*(links coming soon as dashboards are published)*

---

## Data Pipeline

- **ETL scripts (`/src/etl`)**: Python code that pulls JOLTS and CPS series from the BLS API and saves them as clean CSVs (`/data_clean/`).  
- **DuckDB schema (`/src/sql`)**: Builds a consolidated mart (`/data_mart/mart_macro.csv`) with derived KPIs such as Hires per Opening and rolling volatility.  
- **Outputs**: These CSVs feed directly into Tableau dashboards.

---

## Repo Highlights

- `/src/etl` → Python ETL for JOLTS and CPS data  
- `/src/sql` → DuckDB schema & KPI definitions  
- `/data_clean`, `/data_mart` → Clean and mart CSVs for Tableau  
- `/docs` → Experiment logs and notes  
- `/tableau` → Workbook exports

---

## Roadmap

Planned improvements and extensions include:
- Adding remote vs. return-to-office overlays
- Exploring AI-exposure by SOC codes
- Building state-level or regional breakdowns for youth unemployment
- Automating monthly refreshes

---

## Notes

- Data are from publicly available, seasonally adjusted BLS series.  
- Revisions can affect the most recent months; interpretation should account for

git add README.md
git rebase --continue

cat > README.md << 'EOF'
ls -1
eof
