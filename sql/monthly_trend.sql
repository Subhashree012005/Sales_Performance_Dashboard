-- ============================================================
-- monthly_trend.sql
-- Revenue aggregated by month to show trend over time
-- Concepts: STRFTIME (date function), GROUP BY, ORDER BY
-- ============================================================

-- Month-wise revenue trend
SELECT
    STRFTIME('%Y-%m', date)         AS month,          -- extracts "2023-01" from "2023-01-15"
    ROUND(SUM(revenue), 2)          AS monthly_revenue,
    COUNT(order_id)                 AS total_orders,
    SUM(units_sold)                 AS units_sold
FROM sales
GROUP BY month
ORDER BY month ASC;


-- ============================================================
-- BONUS: Quarter-wise revenue
-- Concepts: CASE WHEN, STRFTIME
-- ============================================================

SELECT
    STRFTIME('%Y', date)            AS year,

    CASE
        WHEN CAST(STRFTIME('%m', date) AS INTEGER) BETWEEN 1 AND 3  THEN 'Q1'
        WHEN CAST(STRFTIME('%m', date) AS INTEGER) BETWEEN 4 AND 6  THEN 'Q2'
        WHEN CAST(STRFTIME('%m', date) AS INTEGER) BETWEEN 7 AND 9  THEN 'Q3'
        ELSE 'Q4'
    END                             AS quarter,

    ROUND(SUM(revenue), 2)          AS quarterly_revenue,
    COUNT(order_id)                 AS total_orders

FROM sales
GROUP BY year, quarter
ORDER BY year, quarter;