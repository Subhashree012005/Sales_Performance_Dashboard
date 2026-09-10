import sqlite3
import pandas as pd

# Connect to SQLite (creates file if not exists)
conn = sqlite3.connect("database/sales.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        order_id    TEXT,
        date        TEXT,
        salesperson TEXT,
        region      TEXT,
        product     TEXT,
        units_sold  INTEGER,
        unit_price  REAL,
        revenue     REAL
    )
""")

# Load CSV and insert into DB
df = pd.read_csv("data/sales_data.csv")
df.to_sql("sales", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("Database ready: sales.db")