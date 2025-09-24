-- Build mart from cleaned JOLTS + CPS for Tableau
CREATE OR REPLACE TABLE jolts_us AS SELECT * FROM read_csv_auto('data_clean/jolts_US.csv');
CREATE OR REPLACE TABLE cps_pub   AS SELECT * FROM read_csv_auto('data_clean/cps_published.csv');

CREATE OR REPLACE VIEW v_metrics AS
SELECT 
  j.date,
  j.JOLTS_Openings                       AS openings_mil,
  j.JOLTS_Hires                          AS hires_mil,
  j.JOLTS_QuitsRate                      AS quits_rate_pct,
  j.JOLTS_LayoffsRate                    AS layoffs_rate_pct,
  c.UnempRate_Total                      AS unemp_rate_total,
  c.LFPR_Total                           AS lfpr_total,
  c.EmpPop_Total                         AS emppop_total,
  c.UnempRate_20_24                      AS unemp_rate_20_24,
  c.UnempRate_25_34                      AS unemp_rate_25_34
FROM jolts_us j
LEFT JOIN cps_pub c USING(date)
ORDER BY date;

CREATE OR REPLACE VIEW v_efficiency AS
SELECT date, hires_mil / NULLIF(openings_mil,0) AS hires_per_opening
FROM v_metrics;

CREATE OR REPLACE VIEW v_stability AS
SELECT 
  date,
  STDDEV_SAMP(unemp_rate_total) OVER (ORDER BY date ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS unemp_std6m
FROM v_metrics;

CREATE OR REPLACE TABLE mart_macro AS
SELECT m.*, e.hires_per_opening, s.unemp_std6m
FROM v_metrics m
LEFT JOIN v_efficiency e USING(date)
LEFT JOIN v_stability  s USING(date)
ORDER BY m.date;
