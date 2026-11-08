-- 1. Verify the table size
SELECT COUNT(*) AS total_records
FROM fmcg_retail;

-- 2. Revenue proxy by product category
SELECT
    category,
    SUM(units_sold) AS total_units,
    ROUND(SUM(revenue_proxy), 2) AS revenue_proxy
FROM fmcg_retail
WHERE quality_flag = 0
GROUP BY category
ORDER BY revenue_proxy DESC;

-- 3. Revenue proxy by sales channel
SELECT
    channel,
    SUM(units_sold) AS total_units,
    ROUND(SUM(revenue_proxy), 2) AS revenue_proxy
FROM fmcg_retail
WHERE quality_flag = 0
GROUP BY channel
ORDER BY revenue_proxy DESC;

-- 4. Compare average units sold per record by promotion status
SELECT
    promotion_flag,
    COUNT(*) AS record_count,
    ROUND(AVG(units_sold), 2) AS average_units_per_record,
    ROUND(AVG(price_unit), 2) AS average_unit_price
FROM fmcg_retail
WHERE quality_flag = 0
GROUP BY promotion_flag
ORDER BY promotion_flag;

-- 5. Monthly revenue proxy
SELECT
    substr(date, 1, 7) AS month,
    ROUND(SUM(revenue_proxy), 2) AS revenue_proxy
FROM fmcg_retail
WHERE quality_flag = 0
GROUP BY substr(date, 1, 7)
ORDER BY month;

-- 6. Identify records flagged for investigation
SELECT
    date,
    sku,
    channel,
    region,
    stock_available,
    delivered_qty,
    units_sold
FROM fmcg_retail
WHERE quality_flag = 1;
