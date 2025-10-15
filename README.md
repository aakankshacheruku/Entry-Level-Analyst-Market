# Entry-Level Analyst Market

**Project Type:** Labor Market Analysis  
**Duration:** 7-Day Iterative Build  
**Tools:** Python (Pandas, DuckDB), Tableau, Git, BLS JOLTS/CPS Data  
**Focus:** Entry-Level Analyst Market Trends & AI-Augmented Career Insights  

---

I’m rebuilding this project to gain a deeper understanding of the entry-level data analyst job market and why it has become so challenging to break into. Using public datasets from the Bureau of Labor Statistics (JOLTS + CPS), I’m mapping the reality behind the “no entry-level jobs” sentiment — how openings, hires, and turnover have shifted across analytical occupations over time.

The project is structured as a 7-day iterative blueprint — each day tackles a real problem I’ve run into while building data pipelines, dashboards, and validation logic from scratch. The goal is to demonstrate not only what I built, but also how I learned through trial, error, and iteration.

---

## Why This Project Exists

In 2025, the data world is changing faster than the job market can keep up. Entry-level roles that once served as training grounds for new analysts are being reshaped — not only by competition, but by AI automation and shifting expectations of what “analytical work” means.

This project started as a way to measure that shift — combining public labor data (JOLTS + CPS) to ground the “no entry-level jobs” conversation in numbers. It’s also become a way to rethink what it means to enter the data profession at a time when AI tools can already write SQL, summarize dashboards, and automate reporting.

I don’t see that as a threat. I see it as a redefinition of leverage.  
AI doesn’t erase the analyst’s value — it amplifies judgment, storytelling, and problem framing. Analysts who thrive aren’t the ones who compete with AI for tasks; they’re the ones who use it to scale their own reasoning.

### How entry-level analysts can benefit from AI
- Offload repetitive tasks (parsing, quick EDA, boilerplate SQL) to focus on interpretation and decisions.  
- Pair AI with data validation and skepticism — use it to propose ideas, then verify with sources and checks.  
- Use AI to accelerate iteration cycles (hypotheses → prototypes → feedback) without skipping rigor.  
- Lean into communication: clear narratives, decision memos, “so what?” — where human context wins.

This project isn’t just tracking labor trends; it’s exploring the skills, habits, and mindsets that make early-career analysts resilient in an AI-driven world. It’s an experiment in understanding the data market and adapting to it at the same time.

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

---

## Day 6 – Visualization Layer

### Goal
Transform the aggregate outputs into an interactive Tableau dashboard that visualizes how labor-market conditions for analysts have evolved — highlighting the balance between job openings, hires, and separations over time.

### Dashboard: *Aggregate Labor Market Lens*
Built in **Tableau Public**, this dashboard connects directly to `outputs/dashboard_data.csv` and focuses on three analytical lenses:

#### 1. **Macro Demand Index**
- Line chart of `overall_demand_index` (z-score blend of openings, hires, and employment-to-population ratio)  
- Smoothed 3-month rolling average to emphasize structural trends  
- Color bands highlight expansions vs. contractions in analyst-demand pressure

#### 2. **Labor Flow Dynamics**
- Dual-axis comparison of `openings_rate` vs. `hires_rate`  
- Secondary chart: `hires_rate` vs. `separations_rate`  
- Tooltip KPIs: `openings_to_hires`, `hires_to_separations`, `net_hiring_rate`  
- Rolling volatility overlay for separations → turnover stability signal

#### 3. **Participation & Employment Context**
- Overlay of `participation_rate` and `employment_pop_ratio`  
- Shading to highlight pandemic shock and post-2023 normalization  
- Acts as a proxy for supply-side pressure among early-career analysts

### Design Principles
- Minimal color palette (muted neutrals + accent line for the index)  
- Uniform date axis across all charts for temporal alignment  
- KPI cards at the top summarizing the latest-month values  
- Annotated callouts for key inflection points (e.g., 2020-2021 recovery, 2024 hiring plateau)

### File Outputs
| File | Description |
|-------|-------------|
| `tableau/Day6_Aggregate_Lens.twbx` | Tableau workbook (connected to dashboard_data.csv) |
| `outputs/dashboard_data.csv` | Single source of truth for all visualizations |

### Insights
- **Hiring elasticity weakened post-2023** — openings recovered faster than hires.  
- **Turnover volatility fell**, implying longer job tenures but fewer new entry paths.  
- **Participation rebounded** but hasn’t translated into proportionate hiring, signaling a bottleneck in analyst absorption.

### Next Step (Optional)
When you generate by-occupation data, replicate this dashboard with:
- Filters for `occupation_group`
- Comparison lines for `overall_demand_index` vs. `entry_level_index`
- A calculated field: `entry_level_access_ratio`
This will evolve the visualization from macro to micro.

---

## Day 7 – Reflection & Interpretation

### Goal
Synthesize what the seven-day build reveals about the entry-level analyst market — and about how analysts can adapt in an AI-accelerated labor landscape.

### Key Takeaways

#### 1. **Data Reality**
- Aggregate labor demand remains strong, but **conversion into hires has decoupled** from openings.
- The “no entry-level jobs” sentiment reflects a structural hiring friction, not a total absence of demand.

#### 2. **Analyst Reality**
- Entry-level analysts are now competing on *judgment*, *communication*, and *adaptability* rather than rote data handling.
- The ability to iterate, validate, and explain — faster and cleaner with AI — defines leverage.

#### 3. **Project Lessons**
| Skill | Where It Showed Up | Takeaway |
|-------|--------------------|-----------|
| **ETL Design** | Days 1–3 | Schema consistency > speed; every mismatch compounds downstream |
| **Modeling Logic** | Day 5 | Aggregation clarity beats over-modeling noisy signals |
| **Visualization** | Day 6 | Context drives credibility — clear baselines and annotations matter |
| **Reflection** | Day 7 | Turning data into story makes technical work legible to decision-makers |

### What This Project Proved
1. Public datasets can meaningfully quantify career narratives — if handled with rigor.  
2. AI tools, when paired with statistical reasoning, compress iteration cycles without replacing analysis.  
3. Transparency (open data, reproducible code, documented trade-offs) is itself a professional differentiator.

### Future Roadmap
- Add **entry-level weighting** (age 20–29 × occupation) to compute `entry_level_access_ratio`.  
- Deploy automated refresh pipeline using DuckDB + GitHub Actions.  
- Expand Tableau to **interactive sector breakdowns** (tech, finance, public sector).  
- Publish a full “AI-augmented analyst” write-up synthesizing skill trends.

---

> 🧭 *This 7-day blueprint started as an experiment in data plumbing — it ended as a reflection on what it means to build truthfully in public.  
> The hardest part of entering data isn’t the code; it’s building clarity when the system you’re analyzing keeps changing.  
> That’s what this project — and this dashboard — are ultimately about.*

---

## Backlog / Roadmap
- Add occupation × age CPS dataset for entry-level weighting  
- Integrate Tableau Public dashboards  
- Automate monthly refresh (GitHub Actions + DuckDB)  
- Add AI-assisted anomaly detection (schema drift alerts)
