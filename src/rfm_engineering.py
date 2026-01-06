import pandas as pd


def build_rfm(df: pd.DataFrame, reference_date=None) -> pd.DataFrame:
    """
    Build RFM features:
    - Recency: days since last purchase
    - Frequency: number of invoices
    - Monetary: total spend
    """

    if reference_date is None:
        reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    rfm = (
        df.groupby("CustomerID")
        .agg(
            Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
            Frequency=("InvoiceNo", "nunique"),
            Monetary=("TotalPrice", "sum"),
        )
        .reset_index()
    )

    return rfm
