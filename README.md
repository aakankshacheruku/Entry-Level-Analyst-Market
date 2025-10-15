# Entry-Level Analyst Market

I’m rebuilding this project to gain a deeper understanding of the entry-level data analyst job market and why it has become so challenging to break into. Using public datasets from the Bureau of Labor Statistics (JOLTS + CPS), I’m mapping the reality behind the “no entry-level jobs” sentiment — how openings, hires, and turnover have shifted across analytical occupations over time.

The project is structured as a 7-day iterative blueprint — each day tackles a real problem I’ve run into while building data pipelines, dashboards, and validation logic from scratch. The goal is to demonstrate not only what I built, but also how I learned through trial, error, and iteration.

---

## Why This Project Exists
*(keep your current text here — unchanged)*

---

## 7-Day Structure

| Day | Theme | Focus |
|-----|--------|--------|
| **Day 1** | Data Ingestion & Structure | Pull JOLTS + CPS data and design the relational schema |
| **Day 2** | Cleaning & Validation | Handle missing data, dtype mismatches, and schema drift |
| **Day 3** | Transformation Logic | Merge sources, create derived metrics, normalize categories |
| **Day 4** | Environment Modernization & I/O Resilience | Reproducibility, logging, fault-tolerant I/O |
| **Day 5** | Aggregate Modeling Outputs | Create Tableau-ready labor-demand index |
| **Day 6** | Visualization Layer | Tableau dashboards for labor trends & entry-level dynamics |
| **Day 7** | Reflection & Interpretation | Synthesis: labor data + the AI-augmented analyst |

---

## Day 5 – Aggregate Modeling Outputs

### Goal
Model how hiring and job-opening dynamics evolved for analytical occupations, using public JOLTS and CPS data. This phase produces a unified, Tableau-ready dataset that tracks **labor demand pressure** over time.

### Data
- **JOLTS (aggregate):** openings_rate, hires_rate, separations_rate  
- **CPS (aggregate):** unemployment_rate, participation_rate, employment_pop_ratio

### Key Derived Metrics
| Metric | Definition |
|---------|-------------|
| **Openings-to-Hires** | job openings ÷ hires |
| **Hires-to-Separations** | hires ÷ separations |
| **Net Hiring Rate** | hires − separations |
| **Turnover Volatility** | 12-month rolling SD of separations_rate |
| **Overall Demand Index** | z-score blend of openings_rate, hires_rate, and employment-to-population ratio |

### Outputs
| File | Description |
|------|-------------|
| `jolts_metrics_aggregate.csv` | Base JOLTS rates + derived ratios |
| `cps_metrics_aggregate.csv` | Base CPS labor-force metrics |
| `entry_level_index_aggregate.csv` | Aggregate demand index (entry-level weighting pending) |
| `dashboard_data.csv` | Unified Tableau-ready dataset |

### Next Steps (Entry-Level Upgrade)
Once CPS and JOLTS are available **by occupation × age**, rerun `scripts/day5_modeling.py` to generate entry-level weighted indices (`entry_level_index` and `entry_level_access_ratio`).

### Caveats
- Aggregate indices smooth over sector differences.  
- Entry-level accessibility not yet modeled — proxy planned via age 20–29 employment share.

### Visualization
The companion Tableau dashboard visualizes:
- Aggregate demand index (trend)  
- Labor-flow ratios (openings↔hires↔separations)  
- Participation & employment rates (labor supply context)

### Project Structure (as of Day 5)
job-market-navigator/
├── data/
│ └── processed/
├── outputs/
│ ├── jolts_metrics_aggregate.csv
│ ├── cps_metrics_aggregate.csv
│ ├── entry_level_index_aggregate.csv
│ └── dashboard_data.csv
├── scripts/
│ ├── day5_modeling_aggregate.py
│ └── day5_modeling.py
├── README.md
└── tableau/
└── Day5_Aggregate_Lens.twbx
__________
## Backlog / Roadmap
- Add occupation × age CPS dataset for entry-level weighting  
- Integrate Tableau Public dashboards  
- Automate monthly refresh (GitHub Actions + DuckDB)  
- Add AI-assisted anomaly detection (schema drift alerts)  
