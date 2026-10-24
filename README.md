# Customer Segmentation Using K-Means Clustering

## Project Overview
This project uses the UCI Online Retail II dataset to segment customers based on their purchasing behavior. The objective is to identify groups of customers with similar spending patterns, purchase quantities, and purchasing frequency.

## Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- VS Code

## Project Workflow

### 1. Data Cleaning
- Removed records with missing Customer IDs.
- Investigated cancelled invoices, negative quantities, and nonpositive prices.
- Filtered out cancelled transactions and invalid quantities or prices.
- Investigated and removed exact duplicate transaction rows.

### 2. Feature Engineering
Calculated the following customer-level features:
- **TotalSpent:** total spending per customer.
- **TotalQuantity:** total quantity purchased.
- **InvoiceCount:** number of unique invoices per customer.

### 3. Data Preparation
Applied a `log1p` transformation to reduce feature skewness and used `StandardScaler` to standardize the features.

### 4. Customer Clustering
Applied the K-Means algorithm and compared models with 3, 4, and 5 clusters using the Silhouette Score.

| Number of Clusters | Silhouette Score |
|---:|---:|
| 3 | 0.4147 |
| 4 | 0.3715 |
| 5 | 0.3502 |

The four-cluster model was provisionally selected because it provided more detailed, interpretable customer segments, including a distinct high-value, frequent-customer group.

### 5. Customer Segments
The final model grouped 4,312 customers into four segments:

| Segment | Customers | Percentage |
|---|---:|---:|
| Regular Mid-Value Customers | 1,372 | 31.82% |
| Very Low-Spending Customers | 869 | 20.15% |
| Low-Spending Infrequent Customers | 1,574 | 36.50% |
| High-Value Frequent Customers | 497 | 11.53% |

## Key Findings
- Low-spending, infrequent customers form the largest segment.
- High-value, frequent customers represent 11.53% of the analyzed customer base.
- The three-cluster model achieved a higher Silhouette Score than the four-cluster model.
- The segmentation provides an exploratory basis for customer retention and marketing strategies.

## Project Outputs
- `customer_data.csv` — customer-level purchasing summaries.
- `customer_segments.csv` — customer summaries with assigned clusters and segment names.

## Limitations
The clusters are exploratory and are not proof of customer loyalty or future behavior. Further validation is needed before using the results to make business decisions.

## Dataset
UCI Machine Learning Repository — Online Retail II.

## Author
Data Science Student | Customer Analytics Project
