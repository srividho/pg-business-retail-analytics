# Data Dictionary

## 1. P&G Financial Dataset

Source: Official P&G public financial highlights.

| Field | Meaning | Unit / Format |
|---|---|---|
| fiscal_year | P&G fiscal reporting year | Integer |
| net_sales_usd_bn | Net sales | USD billions |
| operating_income_usd_bn | Operating income | USD billions |

**Derived metrics**

| Metric | Definition |
|---|---|
| Operating margin (%) | Operating income / Net sales × 100 |
| YoY net sales growth (%) | (Current-year sales − Previous-year sales) / Previous-year sales × 100 |

Note: Source figures are rounded and require verification against official reports.

## 2. FMCG Retail Dataset

Source: Third-party synthetic FMCG dataset (2022–2024).

| Field | Meaning | Unit / Format |
|---|---|---|
| date | Sales observation date | Date |
| sku | Product identifier | Text |
| brand | Product brand | Text |
| segment | Product segment | Text |
| category | Product category | Text |
| channel | Sales channel | Text |
| region | Geographic region | Text |
| pack_type | Packaging type | Text |
| price_unit | Recorded unit price | Numeric |
| promotion_flag | Promotion indicator (0/1) | Integer |
| delivery_days | Delivery duration | Numeric |
| stock_available | Available stock | Numeric |
| delivered_qty | Delivered quantity | Numeric |
| units_sold | Units sold | Numeric |

## 3. Derived FMCG Fields

| Field | Meaning |
|---|---|
| quality_flag | Identifies records containing negative stock or quantity values |
| revenue_proxy | price_unit × units_sold |
| month | Calendar month derived from date |
| promotion_status | Label derived from promotion_flag |

## 4. Important Limitations

- The FMCG dataset is synthetic and does not represent actual P&G sales.
- The currency and accounting meaning of price_unit are unverified.
- Revenue proxy is not verified accounting revenue.
- Promotion comparisons are descriptive, not causal.
- Three records with negative stock or quantity values are flagged in the analysis.
