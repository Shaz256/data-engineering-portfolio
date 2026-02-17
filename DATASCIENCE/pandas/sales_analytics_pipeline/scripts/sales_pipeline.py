"""
End-to-End Sales Analytics using Pandas
Author: Shaziya Sayed
Purpose: Demonstrate cleaning, aggregation, sorting, and window logic
"""

import pandas as pd


# =========================================================
# LOAD
# =========================================================
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


# =========================================================
# CLEAN
# =========================================================
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["amount"] = df["amount"].fillna(0)
    return df


# =========================================================
# GROUPBY METRICS
# =========================================================
def customer_metrics(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("customer_id")
        .agg(
            total_spent=("amount", "sum"),
            avg_spent=("amount", "mean"),
            order_count=("order_id", "count"),
        )
        .reset_index()
    )


# =========================================================
# ORDER BY
# =========================================================
def top_transactions(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values("amount", ascending=False)


# =========================================================
# WINDOW-LIKE OPERATIONS
# =========================================================
def window_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.sort_values("order_date")

    # running total
    df["running_total"] = df["amount"].cumsum()

    # rank within region
    df["region_rank"] = (
        df.groupby("region")["amount"]
        .rank(method="dense", ascending=False)
    )

    # lag feature
    df["prev_amount"] = df.groupby("customer_id")["amount"].shift(1)

    # rolling average
    df["rolling_avg_3"] = (
        df["amount"]
        .rolling(window=3, min_periods=1)
        .mean()
    )

    return df


# =========================================================
# MAIN
# =========================================================
def main():

    df = load_data("../data/sales_data.csv")
    df = clean_data(df)

    print("=== Raw ===")
    print(df.head())

    print("\n=== Customer Metrics ===")
    print(customer_metrics(df))

    print("\n=== Top Transactions ===")
    print(top_transactions(df).head())

    print("\n=== Window Features ===")
    print(window_features(df).head())


if __name__ == "__main__":
    main()
