import pandas as pd


def preprocess_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw transaction data:
    - Remove canceled invoices
    - Remove negative / zero quantity and unit price
    - Drop missing CustomerID
    - Convert InvoiceDate to datetime
    - Filter UK market
    - Remove extreme outliers in Quantity
    """

    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    df = df.dropna(subset=["CustomerID"])
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df = df[df["Country"] == "United Kingdom"]
    upper_qty = df["Quantity"].quantile(0.99)
    df = df[df["Quantity"] <= upper_qty]

    return df
