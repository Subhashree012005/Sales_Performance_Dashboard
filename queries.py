import sqlite3
import pandas as pd

DB_PATH = "database/sales.db"

def get_connection():
    return sqlite3.connect(DB_PATH)


def get_kpi_summary():
    query = """
        SELECT
            ROUND(SUM(revenue), 2)   AS total_revenue,
            COUNT(order_id)          AS total_orders,
            SUM(units_sold)          AS total_units_sold,
            ROUND(AVG(revenue), 2)   AS avg_order_value
        FROM sales
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_revenue_by_salesperson():
    query = """
        SELECT
            salesperson,
            ROUND(SUM(revenue), 2)  AS total_revenue,
            COUNT(order_id)         AS total_orders,
            RANK() OVER (ORDER BY SUM(revenue) DESC) AS revenue_rank
        FROM sales
        GROUP BY salesperson
        ORDER BY total_revenue DESC
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_monthly_trend():
    query = """
        SELECT
            STRFTIME('%Y-%m', date)  AS month,
            ROUND(SUM(revenue), 2)   AS monthly_revenue,
            COUNT(order_id)          AS total_orders
        FROM sales
        GROUP BY month
        ORDER BY month ASC
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_region_performance():
    query = """
        SELECT
            region,
            ROUND(SUM(revenue), 2)  AS total_revenue,
            COUNT(order_id)         AS total_orders,
            ROUND(
                SUM(revenue) * 100.0 / (SELECT SUM(revenue) FROM sales), 2
            )                       AS revenue_share_pct
        FROM sales
        GROUP BY region
        ORDER BY total_revenue DESC
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_product_performance():
    query = """
        SELECT
            product,
            ROUND(SUM(revenue), 2)  AS total_revenue,
            SUM(units_sold)         AS total_units
        FROM sales
        GROUP BY product
        ORDER BY total_revenue DESC
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_top_orders():
    query = """
        SELECT
            order_id, date, salesperson,
            region, product, revenue
        FROM sales
        ORDER BY revenue DESC
        LIMIT 10
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_ranked_by_region():
    query = """
        SELECT
            region,
            salesperson,
            ROUND(SUM(revenue), 2)  AS total_revenue,
            RANK() OVER (
                PARTITION BY region
                ORDER BY SUM(revenue) DESC
            )                       AS rank_in_region
        FROM sales
        GROUP BY region, salesperson
        ORDER BY region, rank_in_region
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df