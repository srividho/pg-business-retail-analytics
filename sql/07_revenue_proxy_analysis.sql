-- Revenue proxy by category and sales channel
-- Synthetic dataset; this is not actual P&G revenue.

SELECT
    category,
    channel,
    COUNT(*) AS record_count,
    SUM(units_sold) AS total_units_sold,
    ROUND(AVG(price_unit), 2) AS average_unit_price,
    ROUND(SUM(price_unit * units_sold), 2) AS revenue_proxy,
    ROUND(AVG(price_unit * units_sold), 2) AS average_revenue_proxy_per_record
FROM fmcg_retail
WHERE quality_flag = 0
GROUP BY category, channel
ORDER BY revenue_proxy DESC;
