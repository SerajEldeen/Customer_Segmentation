import pandas as pd
from sklearn.metrics import silhouette_score


def compute_silhouette_score(scaled_features, labels) -> float:
    """
    Compute Silhouette Score for clustering evaluation
    """
    return silhouette_score(scaled_features, labels)


def cluster_summary(rfm_df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate business-friendly cluster summary
    """

    summary = (
        rfm_df.groupby("Cluster")
        .agg(
            Recency_mean=("Recency", "mean"),
            Frequency_mean=("Frequency", "mean"),
            Monetary_mean=("Monetary", "mean"),
            Customer_Count=("CustomerID", "count"),
        )
        .sort_values("Customer_Count", ascending=False)
    )

    summary["Customer_Percentage"] = (
        summary["Customer_Count"] / summary["Customer_Count"].sum() * 100
    )

    return summary
