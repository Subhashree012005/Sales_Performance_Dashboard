-- ============================================================
-- region_performance.sql
-- Revenue, orders, and average order value by region
-- Concepts: GROUP BY, Aggregates, ROUND, ORDER BY
-- ============================================================

-- Region-wise performance summary
SELECT
    region,
    ROUND(SUM(revenue), 2)          AS total_revenue,
    COUNT(order_id)                 AS total_orders,
    SUM(units_sold)                 AS total_units,
    ROUND(AVG(revenue), 2)          AS avg_order_value,
    ROUND(AVG(units_sold), 1)       AS avg_units_per_order
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;


-- ============================================================
-- BONUS: Revenue share % per region
-- Concepts: Subquery, ROUND, division
-- ============================================================

SELECT
    region,
    ROUND(SUM(revenue), 2)                          AS total_revenue,
    COUNT(order_id)                                 AS total_orders,

    -- Revenue as a % of overall total (subquery used here)
    ROUND(
        SUM(revenue) * 100.0 / (SELECT SUM(revenue) FROM sales),
        2
    )                                               AS revenue_share_pct

FROM sales
GROUP BY region
ORDER BY revenue_share_pct DESC;


-- ============================================================
-- BONUS: Product performance within each region
-- Concepts: Multiple GROUP BY columns, ORDER BY multiple cols
-- ============================================================

SELECT
    region,
    product,
    ROUND(SUM(revenue), 2)          AS total_revenue,
    SUM(units_sold)                 AS total_units
FROM sales
GROUP BY region, product
ORDER BY region, total_revenue DESC;