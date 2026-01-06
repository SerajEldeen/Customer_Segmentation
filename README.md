# Customer Segmentation Using RFM Analysis – Unsupervised Machine Learning Project

## Project Overview

This project focuses on **customer segmentation** using **unsupervised learning techniques** applied to real-world transactional data.  
The main objective is to group customers based on purchasing behavior in order to support **data-driven marketing, retention, and personalization strategies**.

The project follows a **professional end-to-end machine learning workflow**, starting from raw transaction data, moving through data cleaning and feature engineering, and ending with interpretable business insights derived from clustering.

---

## Business Objective

- Problem Type: **Unsupervised Learning (Clustering)**
- Business Goal:
  - Understand customer purchasing behavior
  - Identify distinct customer segments
  - Enable targeted marketing and retention strategies
- Core Technique:
  - **RFM Analysis**
    - **Recency**: How recently a customer purchased
    - **Frequency**: How often a customer purchases
    - **Monetary**: How much a customer spends

---

## Dataset Description

The dataset contains transactional data with the following columns:

- `InvoiceNo`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerID`
- `Country`

Each row represents a single transaction item.

To ensure business relevance and data quality:

- Canceled invoices were removed
- Invalid and extreme values were handled
- Analysis focused on the **United Kingdom market**, which contains the majority of transactions

---

## Project Folder Structure

customer-segmentation-rfm/  
├── data/  
│ ├── raw/  
│ │ └── online_retail.csv  
│ └── processed/  
│ ├── customer_segments.csv
│ ├── online_retail_cleaned.csv  
│ └── rfm_features.csv  
│  
├── models/  
│ └── kmeans_model.pkl
├── notebooks/  
│ ├── 01_data_exploration.ipynb  
│ ├── 02_feature_engineering.ipynb  
│ ├── 03_clustring.ipynb  
│ └── 04_evaluation_insights.ipynb  
│  
├── src/  
│ ├── \***\*init\*\***.py  
│ ├── data_preprocessing.py  
│ ├── rfm_engineering.py  
│ ├── clustering.py  
│ └── evaluation.py  
│  
├── reports/  
│ ├── figures/  
│  
├── README.md  
└── .gitignore

This structure cleanly separates **exploration (notebooks)** from **reusable, production-ready code (`src/`)**, following industry standards.

---

## Notebooks Summary

### 01_data_exploration.ipynb

- Explored dataset structure and column meanings
- Identified data quality issues:
  - 25% missing `CustomerID`
  - Canceled invoices (InvoiceNo starting with `C`)
  - Negative and extreme values in `Quantity` and `UnitPrice`
  - `InvoiceDate` stored as object instead of datetime
- Analyzed country distribution and focused analysis on the UK market

---

### 02_feature_engineering.ipynb

- Cleaned transactional data:
  - Removed canceled invoices
  - Removed invalid and extreme values
  - Dropped missing `CustomerID`
  - Converted date fields
- Saved clean transactional dataset for reuse
- Refactored preprocessing logic into reusable functions under `src/`

- Built RFM features per customer:
  - **Recency**: Days since last purchase
  - **Frequency**: Number of unique invoices
  - **Monetary**: Total customer spending
- Created a customer-level dataset suitable for clustering
- Prepared features for scaling and modeling

---

### 03_clustring.ipynb

- Standardized RFM features
- Applied **KMeans clustering**
- Selected the optimal number of clusters
- Assigned each customer to a behavioral segment
- Validated clustering quality using internal evaluation metrics

---

### 04_evaluation_insights.ipynb

- Interpreted clusters from a **business perspective**
- Labeled customer segments based on RFM patterns
- Analyzed customer distribution across clusters
- Derived actionable business recommendations

---

## Customer Segments Overview

| Cluster | Segment Name        | Business Description                                            |
| ------- | ------------------- | --------------------------------------------------------------- |
| 2       | VIP Customers       | High frequency and high spending customers with recent activity |
| 3       | Potential Loyalists | Customers showing increasing purchase frequency                 |
| 1       | Occasional Shoppers | Infrequent buyers with low spending                             |
| 0       | Lost Customers      | Long time since last purchase with low engagement               |

### Customer Distribution

- Occasional Shoppers: **67.7%**
- Lost Customers: **25.1%**
- Potential Loyalists: **7.0%**
- VIP Customers: **0.2%**

This distribution highlights the need for **retention strategies** and **VIP nurturing programs**.

---

## Business Recommendations

- **VIP Customers**

  - Exclusive offers and early access
  - Loyalty rewards to prevent churn

- **Potential Loyalists**

  - Personalized promotions to increase frequency
  - Membership or reward programs

- **Occasional Shoppers**

  - Engagement campaigns to increase purchase frequency
  - Discount-based reactivation strategies

- **Lost Customers**
  - Win-back campaigns
  - Targeted incentives or surveys to understand churn reasons

---

## `src/` Module Overview

- `data_preprocessing.py`
  - Cleans and prepares transactional data
- `rfm_engineering.py`
  - Builds RFM features per customer
- `clustering.py`
  - Applies scaling and KMeans clustering
- `evaluation.py`
  - Evaluates clustering quality and summarizes segments

These modules ensure **reproducibility, scalability, and clean separation of concerns**.

---

## Key Skills Demonstrated

- Unsupervised Machine Learning
- Customer Segmentation
- RFM Analysis
- Data Cleaning & Feature Engineering
- Clustering Evaluation
- Business-Oriented Interpretation
- Professional Project Structuring

---
