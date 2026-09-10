-- ============================================================
-- create_tables.sql
-- Creates the main sales table in SQLite
-- Run this ONCE before loading any data
-- ============================================================

CREATE TABLE IF NOT EXISTS sales (
    order_id    TEXT PRIMARY KEY,   -- unique order identifier e.g. ORD1001
    date        TEXT,               -- format: YYYY-MM-DD
    salesperson TEXT,               -- name of salesperson
    region      TEXT,               -- North / South / East / West
    product     TEXT,               -- Product A / B / C
    units_sold  INTEGER,            -- number of units in this order
    unit_price  REAL,               -- price per unit in rupees
    revenue     REAL                -- total = units_sold * unit_price
);
