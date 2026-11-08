# P&G Business & Retail Analytics — Public Data Case Study

## Overview

This project demonstrates an end-to-end analytics workflow using Python, pandas, SQL, SQLite, Matplotlib, and Power BI.

It contains two separate analytical workstreams:

1. **P&G Financial Analysis:** Analysis of selected financial highlights from official Procter & Gamble public reports (FY2022–FY2026).
2. **FMCG Retail Analytics:** Descriptive analysis of a third-party synthetic retail dataset covering product categories, sales channels, data quality, and promotion groups.

> **Important:** The FMCG dataset is synthetic and does not represent actual P&G sales. The calculated `revenue_proxy` is exploratory and is not verified accounting revenue.

## Objectives

- Analyse annual company-level financial trends.
- Profile and validate structured datasets.
- Use Python and pandas for data processing and analysis.
- Use SQLite and SQL for business queries.
- Compare product categories, sales channels, and promotion groups.
- Build interactive Power BI dashboards.
- Communicate findings, assumptions, and analytical limitations.

## Technology Stack

- Python 3.12
- pandas and NumPy
- Matplotlib
- SQLite and SQL
- Power BI
- Git and GitHub

## Key Findings

Findings below refer to the **synthetic FMCG dataset only**, unless explicitly stated otherwise.

- Yogurt had the largest total revenue proxy among the five categories.
- Juice had the smallest total and substantially fewer records than the other categories.
- Overall unit totals were similar across Retail, E-commerce, and Discount channels.
- Promotion records showed higher average units sold in all 15 category–channel combinations examined.
- Three records with negative stock or quantity values were flagged and excluded from the main descriptive aggregates.

These are descriptive observations about synthetic data, not evidence of actual market performance or causal promotional effects.

## Project Structure

```text
pg-business-retail-analytics/
├── data/
│   ├── raw/
│   │   ├── pg/
│   │   └── fmcg/
│   └── processed/
├── docs/
│   ├── source_register.md
│   └── data_dictionary.md
├── notebooks/
├── reports/
│   ├── business_findings.md
│   └── figures/
├── sql/
│   ├── 03_business_kpis.sql
│   ├── 04_fmcg_analysis.sql
│   ├── 05_promotion_analysis.sql
│   ├── 06_promotion_summary.sql
│   └── 07_revenue_proxy_analysis.sql
└── src/
    ├── analyze_pg_financials.py
    ├── analyze_fmcg.py
    ├── inspect_fmcg_data.py
    ├── validate_pg_data.py
    ├── profile_fmcg_quality.py
    ├── load_pg_sqlite.py
    ├── load_fmcg_sqlite.py
    ├── prepare_powerbi_data.py
    ├── plot_promotion_comparison.py
    ├── plot_promotion_by_channel.py
    └── plot_revenue_proxy.py
```

## Reports and Visualisations

The detailed findings report is available at [`reports/business_findings.md`](reports/business_findings.md).

Current Python visualisations:

- `reports/figures/pg_financial_trends.png` — P&G financial highlights and derived metrics.
- `reports/figures/fmcg_monthly_revenue_proxy.png` — Monthly synthetic FMCG revenue proxy.
- `reports/figures/fmcg_promotion_comparison.png` — Average units by promotion status.
- `reports/figures/promotion_difference_by_channel.png` — Promotion-group differences by category and channel.
- `reports/figures/revenue_proxy_by_category_channel.png` — Revenue proxy by category and sales channel.

## Power BI Dashboards

Two interactive Power BI dashboards were developed and exported as PDF reports.

### 1. FMCG Retail Analytics Dashboard

- Total units sold and category analysis.
- Sales channel comparisons.
- Promotion analysis.
- Region and date filtering.

[View FMCG Dashboard (PDF)](FMCG_Dashboard.pdf)

### 2. P&G Financial Performance Dashboard

- Net sales trends (FY2022–FY2026).
- Operating income trends.
- Operating margin analysis.
- Financial KPI cards and comparisons.

[View P&G Financial Dashboard (PDF)](P%26G%20Financial%20Performance%20Dashboard.pdf)

The repository also includes the original Power BI files (`.pbix`) in the `powerbi/` directory.

## Data Sources

### P&G Public Financial Information

- [P&G Investor Relations — Annual Reports](https://www.pginvestor.com/financials/annual-reports/default.aspx)
- [P&G FY2026 Annual Report](https://s204.q4cdn.com/332108499/files/doc_financials/2026/ar/2026_annual_report.pdf)
- [P&G FY2026 Financial Highlights](https://us.pg.com/annualreport2026/financial-highlights/)

The project uses rounded financial highlights for FY2022–FY2026.

### Synthetic FMCG Dataset

- [FMCG Daily Sales Data (2022–2024) — Kaggle](https://www.kaggle.com/datasets/beatafaron/fmcg-daily-sales-data-to-2022-2024)

See [`docs/source_register.md`](docs/source_register.md) for source details and limitations.

## Data Quality and Methodology

- The raw FMCG source file is preserved unchanged.
- Records with negative values in `stock_available`, `delivered_qty`, or `units_sold` are flagged.
- The main descriptive FMCG aggregates exclude the three flagged records (`quality_flag = 0`).
- `revenue_proxy` is calculated as `price_unit × units_sold`.
- January 2022 covers only part of the month because the dataset begins on 21 January 2022.
- Promotion comparisons are descriptive and do not establish causation.
- P&G financial metrics are based on rounded published headline values.

Negative quantity values can represent returns or adjustments in real systems. Their meaning is not confirmed in this synthetic dataset, so the records are flagged rather than silently altered.

## Reproducibility

Run commands from the project root.

### Environment Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Data Setup

Obtain the source datasets from the documented sources, subject to their licences, and place them in the paths expected by the scripts.

Raw and processed datasets are excluded from Git. They must be obtained or regenerated locally before running the complete workflow.

Run the Python validation and analysis scripts, load the data into SQLite, execute the SQL files, and regenerate the visualisations.

## Limitations

- The FMCG dataset is synthetic and is not actual P&G or real-world retail transaction data.
- `price_unit × units_sold` is an unverified revenue proxy; currency and accounting treatment are not confirmed.
- Descriptive promotion differences do not prove that promotions caused higher sales.
- The three negative-value records have uncertain business meaning.
- Group totals depend partly on record counts and data coverage.
- P&G financial highlights use rounded figures.
- The FMCG dataset licence must be checked before redistribution.


## Portfolio Summary

Developed a public-data analytics case study using Python, pandas, Matplotlib, SQLite, SQL, and Power BI. Analysed selected P&G financial highlights separately from a third-party synthetic FMCG dataset. Performed data-quality profiling, category and channel analysis, promotion-group comparisons, SQL querying, and interactive dashboard development while documenting assumptions and avoiding unsupported causal claims.
