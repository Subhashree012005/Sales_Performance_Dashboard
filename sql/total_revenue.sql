-- ============================================================
-- total_revenue.sql
-- KPI Summary: Total revenue, total orders, total units sold
-- Concepts: Aggregate functions (SUM, COUNT, ROUND, AVG)
-- ============================================================

SELECT
    ROUND(SUM(revenue), 2)     AS total_revenue,
    COUNT(order_id)            AS total_orders,
    SUM(units_sold)            AS total_units_sold,
    ROUND(AVG(revenue), 2)     AS avg_order_value
FROM sales;