-- Compare promotion and non-promotion records
-- within each category and channel.

SELECT
    category,
    channel,
    promotion_flag,
    COUNT(*) AS record_count,
    ROUND(AVG(units_sold), 2) AS avg_units_per_record,
    ROUND(AVG(price_unit), 2) AS avg_unit_price,
    ROUND(AVG(revenue_proxy), 2) AS avg_revenue_proxy
FROM fmcg_retail
WHERE quality_flag = 0
GROUP BY
    category,
    channel,
    promotion_flag
ORDER BY
    category,
    channel,
    promotion_flag;
