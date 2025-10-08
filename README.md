# Entry-Level Analyst Market

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

Each day builds toward a more reliable, transparent, and insight-driven data pipeline:

| Day | Theme | Focus |
|-----|--------|--------|
| **Day 1** | Data Ingestion & Structure | Pull JOLTS + CPS data and design the relational schema |
| **Day 2** | Cleaning & Validation | Handle missing data, dtype mismatches, and schema drift |
| **Day 3** | Transformation Logic | Merge sources, create derived metrics, normalize categories |
| **Day 4** | Environment Modernization & I/O Resilience | Reproducibility, logging, fault-tolerant I/O |
| **Day 5** | Metrics & Modeling | Early-career metrics (hiring ratios, opportunity indices) |
| **Day 6** | Visualization Layer | Tableau dashboards for labor trends and entry-level dynamics |
| **Day 7** | Reflection & Interpretation | Synthesis: labor data + the AI-augmented analyst |

---

## Day 4: Environment Modernization & I/O Resilience

**Objective**  
Make the project environment-agnostic, resilient to I/O errors, and easy to run anywhere — so the pipeline doesn’t break on bad inputs or dependency drift.

**What I’m adding in Day 4 (scope):**
- Reproducible environment: one-command setup and consistent dependency versions.  
- Resilient file I/O: a safe CSV reader that gracefully handles malformed rows, missing files, and parser errors.  
- Centralized logging: timestamps, levels, and summaries to make failures obvious and debuggable.  
- Lightweight tests and fixtures: intentionally broken CSVs to prove the I/O layer fails safely.

**Planned file additions (high-level):**
