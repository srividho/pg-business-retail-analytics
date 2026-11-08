WITH promotion_summary AS (
    SELECT
        category,
        channel,
        promotion_flag,
        COUNT(*) AS record_count,
        AVG(units_sold) AS avg_units
    FROM fmcg_retail
    WHERE quality_flag = 0
    GROUP BY category, channel, promotion_flag
),
comparison AS (
    SELECT
        category,
        channel,
        MAX(CASE WHEN promotion_flag = 0
            THEN record_count END) AS non_promo_records,
        MAX(CASE WHEN promotion_flag = 1
            THEN record_count END) AS promo_records,
        MAX(CASE WHEN promotion_flag = 0
            THEN avg_units END) AS non_promo_avg_units,
        MAX(CASE WHEN promotion_flag = 1
            THEN avg_units END) AS promo_avg_units
    FROM promotion_summary
    GROUP BY category, channel
)
SELECT
    category,
    channel,
    non_promo_records,
    promo_records,
    ROUND(non_promo_avg_units, 2) AS non_promo_avg_units,
    ROUND(promo_avg_units, 2) AS promo_avg_units,
    ROUND(
        100.0 * (promo_avg_units - non_promo_avg_units)
        / NULLIF(non_promo_avg_units, 0),
        2
    ) AS observed_unit_difference_pct
FROM comparison
ORDER BY observed_unit_difference_pct DESC;
