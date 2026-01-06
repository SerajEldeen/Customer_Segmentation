import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def run_kmeans(rfm_df: pd.DataFrame, n_clusters: int = 4, random_state: int = 42):
    """
    Scale RFM features and apply KMeans clustering
    """

    features = rfm_df[["Recency", "Frequency", "Monetary"]]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10
    )

    clusters = kmeans.fit_predict(scaled_features)

    rfm_df["Cluster"] = clusters

    return rfm_df, kmeans, scaler
