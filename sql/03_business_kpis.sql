-- 1. Review the financial data
SELECT *
FROM pg_financials
ORDER BY fiscal_year;

-- 2. Calculate operating margin
SELECT
    fiscal_year,
    net_sales_usd_bn,
    operating_income_usd_bn,
    ROUND(
        operating_income_usd_bn * 100.0 / net_sales_usd_bn,
        2
    ) AS operating_margin_pct
FROM pg_financials
ORDER BY fiscal_year;

-- 3. Calculate year-over-year net sales growth
SELECT
    fiscal_year,
    net_sales_usd_bn,
    ROUND(
        (
            net_sales_usd_bn -
            LAG(net_sales_usd_bn) OVER (ORDER BY fiscal_year)
        ) * 100.0 /
        LAG(net_sales_usd_bn) OVER (ORDER BY fiscal_year),
        2
    ) AS net_sales_growth_pct
FROM pg_financials
ORDER BY fiscal_year;
