-- ============================================================
-- top_salesperson.sql
-- Revenue breakdown by each salesperson
-- Concepts: GROUP BY, ORDER BY, SUM, COUNT, ROUND
-- ============================================================

SELECT
    salesperson,
    ROUND(SUM(revenue), 2)          AS total_revenue,
    COUNT(order_id)                 AS total_orders,
    SUM(units_sold)                 AS total_units,
    ROUND(AVG(revenue), 2)          AS avg_order_value,

    -- Window function: rank each salesperson by revenue (best = rank 1)
    RANK() OVER (
        ORDER BY SUM(revenue) DESC
    )                               AS revenue_rank

FROM sales
GROUP BY salesperson
ORDER BY total_revenue DESC;


-- ============================================================
-- BONUS: Salesperson rank WITHIN each region
-- Concepts: RANK() OVER (PARTITION BY ...) — window function
-- This is the query that impresses interviewers the most
-- ============================================================

SELECT
    region,
    salesperson,
    ROUND(SUM(revenue), 2)          AS total_revenue,
    COUNT(order_id)                 AS total_orders,

    -- Resets rank counter for every region independently
    RANK() OVER (
        PARTITION BY region
        ORDER BY SUM(revenue) DESC
    )                               AS rank_in_region

FROM sales
GROUP BY region, salesperson
ORDER BY region, rank_in_region;