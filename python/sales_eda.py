"""Beginner-friendly sales EDA example.
Run: python python/sales_eda.py
"""
import pandas as pd
import matplotlib.pyplot as plt

# Small synthetic dataset so the example runs without external data.
df = pd.DataFrame({
    "date": pd.to_datetime(["2026-01-05", "2026-01-08", "2026-02-02", "2026-02-15", "2026-03-03", "2026-03-20"]),
    "category": ["Electronics", "Books", "Electronics", "Home", "Books", "Home"],
    "region": ["East", "West", "East", "South", "West", "South"],
    "units": [3, 8, 5, 4, 10, 6],
    "unit_price": [500, 200, 450, 300, 180, 320],
})

# 1. Data quality checks
print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicates:", df.duplicated().sum())

# 2. Feature engineering
df["revenue"] = df["units"] * df["unit_price"]
df["month"] = df["date"].dt.to_period("M").astype(str)

# 3. Business summaries
print("\nRevenue by category:\n", df.groupby("category")["revenue"].sum().sort_values(ascending=False))
print("\nRevenue by region:\n", df.groupby("region")["revenue"].sum().sort_values(ascending=False))
print("\nMonthly revenue:\n", df.groupby("month")["revenue"].sum())

# 4. Visualization
monthly = df.groupby("month", as_index=False)["revenue"].sum()
monthly.plot(x="month", y="revenue", kind="bar", legend=False)
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
