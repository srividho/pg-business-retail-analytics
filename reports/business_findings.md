# FMCG Business Findings Report

## P&G Business & Retail Analytics --- Public Data Case Study

**Project status:** Data analysis, SQL queries, visualisations, Power BI dashboards, and GitHub publication completed.
**Prepared by:** Sriram VELMURUGAN
**Tools:** Python, pandas, NumPy, Matplotlib, SQLite, SQL, Power BI, Git and GitHub
**Dataset period:** 21 January 2022 – 31 December 2024

------------------------------------------------------------------------

## 1. Executive summary

This project combines two distinct analytical workstreams:

1.  **P&G public financial analysis:** a year-by-year view of selected
    financial highlights reported by The Procter & Gamble Company.
2.  **Synthetic FMCG retail analysis:** descriptive analysis of a
    third-party synthetic dataset containing product, channel, region,
    promotion, stock, delivery, and unit-sales fields.

The two workstreams are deliberately kept separate. The FMCG dataset is
**not actual P&G sales data** and must not be represented as such. Its
calculated `revenue_proxy` is the product of `price_unit` and
`units_sold`; the source does not establish that this field is
accounting revenue or specify a confirmed currency. It is therefore
described as a *revenue proxy*, not revenue.

The synthetic FMCG analysis found that: - Yogurt had the largest total
revenue proxy among the five categories in the analysed dataset. - Juice
had the smallest total revenue proxy and substantially fewer records
than the other categories. - Channel totals within each category were
relatively close compared with differences between categories. - Records
marked as promotional had higher average units sold than non-promotional
records in all 15 category--channel combinations examined. - Three
records contained negative values in stock or quantity fields. These
records were flagged and excluded from the main descriptive aggregates,
while the raw source data was preserved.

These findings describe the supplied dataset only. Because the dataset
is synthetic, its patterns may reflect its generation rules and should
not be interpreted as evidence of real consumer behaviour or as causal
effects of promotions.

## 2. Project objectives

The project is intended to demonstrate practical business and data
analytics skills relevant to marketing technology, retail analytics, and
data-driven decision support.

Objectives: - Import and inspect public and third-party datasets. -
Document sources, field meanings, and limitations. - Profile data
quality before analysing results. - Use Python and pandas for cleaning,
transformation, aggregation, and charting. - Use SQLite and SQL for
repeatable analytical queries. - Compare categories, channels, and
promotion groups descriptively. - Communicate results with appropriately
qualified conclusions. - Produce a reproducible, GitHub-ready project
and a future dashboard.

## 3. Data sources and scope

### 3.1 P&G public financial highlights

Official source links: - [P&G Investor Relations --- Annual
Reports](https://www.pginvestor.com/financials/annual-reports/default.aspx) -
[P&G FY2026 Annual Report
(PDF)](https://s204.q4cdn.com/332108499/files/doc_financials/2026/ar/2026_annual_report.pdf) -
[P&G FY2026 Financial
Highlights](https://us.pg.com/annualreport2026/financial-highlights/)

The project contains selected annual financial highlights for fiscal years 2022–2026. The ten rounded values for net sales and operating income were checked against P&G's official FY2026 Financial Highlights page.

The figures are rounded company-level financial measures and are used for exploratory trend analysis. Derived metrics, including year-over-year net-sales growth and operating margin, are calculated from these rounded values.

**Important:** these are company-level financial measures, not
product-level retail sales, and should not be combined with the
synthetic FMCG figures as if they share the same scope or units.

### 3.2 Synthetic FMCG retail dataset

Dataset listing: - [FMCG Daily Sales Data (2022--2024) ---
Kaggle](https://www.kaggle.com/datasets/beatafaron/fmcg-daily-sales-data-to-2022-2024)

The dataset was described by its publisher as synthetic. Its rows
contain daily-style product and sales observations across categories,
channels, and regions. The analysed file contains 190,757 rows and 14
columns.

The dataset's licence and redistribution permissions should be verified
before committing the raw file to a public repository. The project
should include the source URL and attribution, and should avoid
redistributing the original data if its licence does not permit it.

### 3.3 Separation of the two workstreams

  ------------------------------------------------------------------------
  Workstream        Data type         Purpose            What it does not
                                                         represent
  ----------------- ----------------- ------------------ -----------------
  P&G financial     Public            Explore annual     Product-level or
  highlights        company-level     sales and          channel-level
                    reported figures, operating-income   sales
                    entered as        trends             
                    rounded values                       

  FMCG retail       Third-party       Demonstrate        Actual P&G
  analysis          synthetic data    retail-style       transactions,
                                      analysis           customers, or
                                      techniques         performance
  ------------------------------------------------------------------------

## 4. Methods and tools

### 4.1 Python analysis

Python scripts are used to: - Read source CSV files. - Parse dates and
derive calendar months. - Flag records containing negative stock or
quantity values. - Calculate descriptive aggregates. - Create charts
with Matplotlib. - Save analysed data for SQL queries.

Libraries include pandas, NumPy, and Matplotlib.

### 4.2 SQLite and SQL

The processed dataset is loaded into SQLite for repeatable analysis. SQL
queries calculate: - Category-level and channel-level totals. - Record
counts and unit totals. - Average unit prices. - Revenue proxies. -
Promotion-group averages and percentage differences. - Monthly
revenue-proxy summaries. - Counts and details of flagged records.

### 4.3 Data-quality approach

The source CSV is preserved unchanged. The analysis creates a quality
flag for records where one or more of `stock_available`,
`delivered_qty`, or `units_sold` is negative. The three flagged records
are excluded from the main aggregates using `WHERE quality_flag = 0`.

This is a transparent analysis choice, not proof that the records are
invalid. Negative quantities can sometimes represent returns or
adjustments in real systems. The source does not provide enough context
to establish that interpretation here, so the records are flagged rather
than silently changed or deleted.

## 5. Data profile and quality findings

### 5.1 Dataset overview

  -----------------------------------------------------------------------
  Check                               Result
  ----------------------------------- -----------------------------------
  Number of rows                      190,757

  Number of columns                   14

  Earliest date                       2022-01-21

  Latest date                         2024-12-31

  Missing values in inspected fields  0

  Invalid parsed dates                0

  Exact duplicate rows                0

  Records with negative stock or      3
  quantity values                     

  Repeated                            None found in the profiling check
  date--SKU--channel--region--pack    
  combination                         
  -----------------------------------------------------------------------

The dataset covers five categories: Yogurt, Milk, ReadyMeal, SnackBar,
and Juice. It includes 14 brands, three sales channels (Retail,
E-commerce, and Discount), three regions, and three pack types.

### 5.2 Flagged records

The quality profile identified three records with negative values:

  ---------------------------------------------------------------------------------
  Date         SKU      Channel    Region             Stock   Delivered  Units sold
                                                  available    quantity 
  ------------ -------- ---------- ------------ ----------- ----------- -----------
  2023-07-26   SN-028   Discount   PL-South              -2          -3          -3

  2023-09-21   SN-010   Retail     PL-Central           -12         -11         -25

  2024-03-14   RE-007   Discount   PL-Central            -6          -7          -8
  ---------------------------------------------------------------------------------

The raw records were retained. The main category, channel, and promotion
summaries exclude these three rows. A sensitivity check showed that the
total units sold were 3,799,824 including the flagged rows and 3,799,860
excluding them. The corresponding revenue-proxy totals were
19,951,300.58 including them and 19,951,543.35 excluding them. These
totals are dataset calculations, not verified financial revenue.

## 6. Category-level findings

The following values exclude the three flagged records.

  Category      Units sold   Revenue proxy   Average unit price
  ----------- ------------ --------------- --------------------
  Yogurt         1,566,582    8,226,193.31                 5.26
  Milk             782,734    4,095,375.42                 5.23
  ReadyMeal        678,842    3,576,348.06                 5.27
  SnackBar         647,353    3,401,349.29                 5.25
  Juice            124,349      652,277.27                 5.27

### Interpretation

-   Yogurt has the highest total units sold and revenue proxy in this
    dataset.
-   Milk is the second-largest category by both measures.
-   Juice has the smallest totals and fewer records than the other
    categories.
-   Average unit prices are close across categories, so differences in
    total proxy are more closely associated with recorded quantities and
    record coverage than with large differences in average price.

These observations are descriptive. Because the dataset is synthetic,
they should not be generalised to the FMCG market.

## 7. Channel-level findings

The following figures exclude the three flagged records.

  Channel        Units sold   Revenue proxy
  ------------ ------------ ---------------
  Retail          1,267,321    6,655,807.06
  E-commerce      1,268,738    6,653,435.41
  Discount        1,263,801    6,642,300.88

### Interpretation

Overall channel totals are very similar in the analysed data. E-commerce
has the highest unit total, while Retail has the highest revenue proxy.
The differences are small relative to the totals.

This comparison does not establish that one channel is more effective or
profitable. The dataset does not provide confirmed costs, margins,
marketing spend, customer counts, or channel-specific business context.

## 8. Category and channel revenue-proxy analysis

The SQL analysis groups the data by category and channel and calculates
record count, unit total, average unit price, revenue proxy, and average
revenue proxy per record.

### 8.1 Main observations

-   Yogurt is the largest category in each of the three channels, with
    channel revenue proxies of approximately 2.73--2.76 million.
-   Milk is the second-largest category, with channel totals of
    approximately 1.36--1.38 million.
-   ReadyMeal and SnackBar have lower totals, around 1.12--1.20 million
    per category--channel group.
-   Juice has the smallest totals, around 0.21--0.22 million per
    channel.

### 8.2 Why record counts matter

Total values are affected by the number of observations in each group.
Juice has substantially fewer records than the other categories, so its
smaller total should not automatically be interpreted as poor
performance. Average revenue proxy per record is one complementary
metric, but it is still affected by the dataset's construction and
should not be treated as a real-world profitability measure.

## 9. Promotion comparison

### 9.1 Overall comparison

  -----------------------------------------------------------------------
  Promotion            Record count Average units sold Average unit price
  status                                               
  -------------- ------------------ ------------------ ------------------
  No promotion              162,294              17.44               5.25

  Promotion                  28,460              34.06               5.27
  -----------------------------------------------------------------------

The average units sold per record are higher in the promotion group. The
average unit prices are similar in the two groups.

### 9.2 Category and channel comparison

The SQL analysis compared average units for each of five categories
across three channels, giving 15 category--channel combinations. All 15
showed a higher average number of units per record in the promotion
group.

The observed percentage differences ranged from approximately +84% to
+102%. The largest was Juice--Retail at about +101.93%; the smallest was
Juice--E-commerce at about +84.03%.

### 9.3 Interpretation and caution

These results are an **observed difference**, not a measured causal
promotion effect. The unusually consistent pattern may reflect the way
the synthetic data was generated. A real promotion-effect study would
require a defensible experimental or quasi-experimental design and
controls for confounding factors such as seasonality, product, store,
price changes, distribution, stock availability, and campaign targeting.

For a real business analysis, useful next steps would include: - Compare
like-for-like products and periods. - Check sample sizes and the
distribution of units sold. - Examine stock availability and potential
stockouts. - Include time, price, region, and product controls. - Use an
appropriate experimental design or causal-inference method if the
business question is causal.

## 10. Monthly trend analysis

The project creates a monthly revenue-proxy chart from the synthetic
dataset. The raw dataset begins on 21 January 2022, so January 2022 is a
partial month and should not be compared directly with full months
without adjustment.

The monthly totals change substantially over the period. Before drawing
conclusions about growth, seasonality, or demand, check the number of
records and date coverage per month. A changing number of records can
drive changes in monthly totals. Because the dataset is synthetic, the
trend should be presented as a data exploration result, not a forecast
or a claim about real retail demand.

## 11. Visualisations created

The project currently includes these figure files:

1.  `reports/figures/pg_financial_trends.png` --- annual P&G financial
    highlights and derived metrics.
2.  `reports/figures/fmcg_monthly_revenue_proxy.png` --- monthly
    synthetic FMCG revenue proxy.
3.  `reports/figures/fmcg_promotion_comparison.png` --- average units
    sold by category and promotion status.
4.  `reports/figures/promotion_difference_by_channel.png` --- observed
    percentage difference in average units by category and channel.
5.  `reports/figures/revenue_proxy_by_category_channel.png` --- revenue
    proxy by category and sales channel.

Charts should retain labels and caveats that identify synthetic data and
avoid causal language.

## 12. P&G financial analysis: reporting notes

The P&G financial analysis uses selected annual financial highlights for FY2022–FY2026.

- The ten rounded net sales and operating income values were verified against the official P&G FY2026 Financial Highlights.
- Year-over-year net-sales growth is calculated from consecutive annual net-sales figures.
- Operating margin is calculated as operating income divided by net sales, multiplied by 100.
- Rounded source figures can create small differences compared with calculations using exact financial statement values.
- These company-level financial measures do not establish product-level, channel-level, or marketing-campaign performance.

## 13. Limitations

1.  **Synthetic FMCG data:** results cannot be presented as actual P&G
    or real-world retail performance.
2.  **Revenue proxy:** `price_unit × units_sold` is not verified
    accounting revenue; currency and treatment of discounts, taxes,
    returns, and other adjustments are not confirmed.
3.  **Potential synthetic patterns:** consistent promotion differences
    may be built into the data-generation process.
4.  **No causal inference:** descriptive group differences do not prove
    that promotions caused higher sales.
5.  **Record-count effects:** group totals depend on how many
    observations each group contains.
6.  **Data-quality ambiguity:** negative quantity and stock values were
    flagged but their business meaning is unknown.
7.  **Monthly coverage:** January 2022 is partial; record counts and
    coverage should be reviewed before comparing months.
8.  **Financial source precision:** the P&G CSV uses rounded figures and
    needs final source-level verification before public release.
9.  **Licence and redistribution:** verify the Kaggle dataset's licence
    before including the raw data in a public repository.
10. **No margin or cost data:** the analysis cannot establish
    profitability, campaign ROI, or channel contribution margin.

## 14. Recommendations

### 14.1 Recommendations based on the synthetic dataset

The following recommendations are analytical considerations derived from the dataset. They are not validated business decisions or recommendations for P&G's actual operations.

**1. Investigate category-level performance**

Yogurt represents the largest category by recorded units sold and revenue proxy, while Juice has the smallest totals.

For a real retail business, investigate whether these differences are associated with product demand, distribution coverage, product availability, pricing, or differences in transaction volume.

**2. Evaluate sales channels using additional performance indicators**

The three channels have relatively similar total units sold and revenue proxies in this dataset.

A real channel-performance assessment should also consider gross margin, fulfilment costs, customer acquisition costs, returns, and order volumes before identifying the most effective channel.

**3. Conduct a controlled promotion effectiveness analysis**

Promotional records show higher average units sold across all 15 category–channel combinations.

This is an observed association in synthetic data, not proof of promotional effectiveness.

For real campaign evaluation, compare similar products and periods, account for seasonality and stock availability, and use an appropriate experimental or quasi-experimental design.

**4. Strengthen inventory and data-quality monitoring**

Three records contain negative stock or quantity values.

A production analytics pipeline should implement automated validation rules, anomaly reporting, and documented handling procedures. Negative values should be investigated rather than automatically deleted because they may represent legitimate returns or adjustments.

**5. Improve reporting consistency**

Monthly totals should be interpreted alongside record counts and data coverage. Partial periods, missing observations, and changes in reporting volume can distort comparisons.

A real business dashboard should display data completeness indicators alongside key performance metrics.

### 14.2 Additional data required for real business decisions

A more reliable retail and marketing analysis would benefit from:

- Transaction-level sales and order identifiers.
- Product costs and gross margins.
- Actual discounts and campaign expenditure.
- Campaign identifiers and campaign dates.
- Inventory availability and stockout records.
- Store, market, and customer-segment information.
- Returns, cancellations, and fulfilment costs.

These fields would support more meaningful analysis of product performance, channel contribution, promotion effectiveness, and profitability.

### 14.3 Portfolio project improvements

The completed project demonstrates the following capabilities:

- Python-based data profiling and descriptive analysis.
- SQL-based business aggregation using SQLite.
- Financial trend analysis using public P&G information.
- Data-quality flagging and validation.
- Power BI dashboard development.
- Documentation of sources, assumptions, and limitations.

Potential future enhancements include automated data-quality tests, monthly coverage monitoring, and a more reproducible data-refresh workflow.

## 15. Reproducibility and project structure

Relevant project files include:

``` text
pg-business-retail-analytics/
├── README.md
├── docs/
│   ├── source_register.md
│   └── data_dictionary.md
├── data/
│   ├── raw/
│   │   ├── pg/
│   │   └── fmcg/
│   └── processed/
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
    ├── validate_pg_data.py
    ├── analyze_fmcg.py
    ├── profile_fmcg_quality.py
    ├── load_pg_sqlite.py
    ├── load_fmcg_sqlite.py
    ├── plot_promotion_comparison.py
    ├── plot_promotion_by_channel.py
    └── plot_revenue_proxy.py
```

This is a working inventory; confirm that each listed file exists before
treating the structure as final.

To reproduce the analysis: 1. Create and activate the project's Python
virtual environment. 2. Install the required Python dependencies. 3.
Obtain the source datasets from their documented sources, subject to
their licences. 4. Run the validation and analysis scripts from the
project root. 5. Load the processed data into SQLite. 6. Run the SQL
files against the generated database. 7. Regenerate the figures and
compare outputs with the documented findings.

The exact command sequence and dependency versions should be documented
in the repository README before publication.

## 16. Conclusion

This project demonstrates an end-to-end descriptive analytics workflow:
source documentation, data profiling, quality flagging, Python-based
analysis, SQL aggregation, and visual communication.

The strongest portfolio story is not that the synthetic data proves a
particular marketing strategy works. It is that the analysis was
conducted transparently: the dataset was inspected, questionable records
were flagged, metrics were defined, results were cross-checked across
Python and SQL, and conclusions were limited to what the data can
support.

The project should be presented as a **public-data and synthetic-data
analytics case study**, with P&G's official financial information
clearly separated from the synthetic FMCG exercise.

------------------------------------------------------------------------

## Appendix A --- Metric definitions

  -----------------------------------------------------------------------------------------------------------------------------------------------
  Metric                  Definition                                                                                      Caveat
  ----------------------- ----------------------------------------------------------------------------------------------- -----------------------
  Total units sold        Sum of `units_sold` after the chosen quality filter                                             Depends on dataset
                                                                                                                          design and record
                                                                                                                          coverage

  Average unit price      Mean of `price_unit`                                                                            Currency and price
                                                                                                                          semantics should be
                                                                                                                          confirmed

  Revenue proxy           Sum of `price_unit × units_sold`                                                                Not verified accounting
                                                                                                                          revenue

  Average revenue proxy   Mean of `price_unit × units_sold`                                                               Sensitive to record
  per record                                                                                                              granularity and
                                                                                                                          synthetic design

  Promotion difference    `(promotion average units − non-promotion average units) / non-promotion average units × 100`   Descriptive association
  (%)                                                                                                                     only, not causal uplift

  Operating margin        `operating income / net sales × 100`                                                            Use source figures and
                                                                                                                          definitions
                                                                                                                          consistently

  Year-over-year          `(current-year net sales − prior-year net sales) / prior-year net sales × 100`                  Rounded inputs affect
  net-sales growth (%)                                                                                                    the result
  -----------------------------------------------------------------------------------------------------------------------------------------------

## Appendix B --- Suggested portfolio description

**P&G Business & Retail Analytics --- Public Data Case Study**

Built a reproducible analytics workflow using Python, pandas,
Matplotlib, SQLite, and SQL. Analysed selected P&G public financial
highlights separately from a third-party synthetic FMCG dataset.
Performed data-quality profiling, category and channel aggregation,
promotion-group comparisons, and charting. Documented source
limitations, flagged anomalous records, and avoided causal claims
unsupported by the data.

**Data integrity note:** The FMCG dataset is synthetic and is not actual
P&G sales data. The calculated revenue proxy is exploratory and should
not be interpreted as verified revenue.
