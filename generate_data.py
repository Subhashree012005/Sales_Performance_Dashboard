import pandas as pd
import numpy as np
import random

np.random.seed(42)

salespeople = ["Ravi Kumar", "Priya Sharma", "Aman Verma", "Sneha Iyer", "Rohit Das"]
regions     = ["North", "South", "East", "West"]
products    = ["Product A", "Product B", "Product C"]

rows = []
for _ in range(500):
    date   = pd.Timestamp("2023-01-01") + pd.Timedelta(days=random.randint(0, 364))
    rows.append({
        "order_id":    f"ORD{random.randint(1000,9999)}",
        "date":        date.strftime("%Y-%m-%d"),
        "salesperson": random.choice(salespeople),
        "region":      random.choice(regions),
        "product":     random.choice(products),
        "units_sold":  random.randint(1, 20),
        "unit_price":  random.choice([500, 1000, 1500, 2000]),
        "revenue":     0   # calculated below
    })

df = pd.DataFrame(rows)
df["revenue"] = df["units_sold"] * df["unit_price"]
df.to_csv("data/sales_data.csv", index=False)
print("Dataset created: 500 rows")