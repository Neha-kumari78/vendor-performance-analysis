# Vendor Performance Analysis

End-to-end vendor analytics project using Python, SQL (SQLite) and Power BI.

## Business Problem
Which vendors drive profit, and where is capital locked in unsold inventory?

## Tech Stack
Python (Pandas, SQLAlchemy, SciPy, Seaborn), SQL (CTEs, joins), SQLite, Power BI (DAX)

## Approach
1. Ingested large CSV files (12.8M+ sales rows) in chunks into SQLite, with logging
2. Built a vendor-level summary using SQL CTEs and joins
3. Engineered KPIs: Gross Profit, Profit Margin, Stock Turnover, Unsold Inventory Value
4. EDA, correlation analysis, hypothesis testing and 95% confidence intervals
5. Designed a Power BI dashboard (Executive Summary, Inventory & Efficiency)

## Key Findings
- Top 10 vendors control about 66% of procurement (supplier dependency risk)
- About $9.55M of capital is locked in unsold inventory
- Overall profit margin is about 30.4%
- Large orders cost about 60% less per unit than small orders
- Low-sales brands show higher margins (candidates for promotion)

## Repository Contents
| File | Description |
|---|---|
| `ingestion_db.py` | Loads raw CSVs into SQLite in chunks |
| `get_vendor_summary.py` | Builds and cleans the vendor summary table |
| `Explolatry_data_analysis.ipynb` | Exploratory data analysis |
| `vendor_perfomance_analysis.ipynb` | Vendor performance analysis and statistics |
| `vendor_sales_summary.csv` | Final vendor summary data |
| `Vendor_perfomnce_dashboard.pdf` | Power BI dashboard export |

## Dashboard
See `Vendor_perfomnce_dashboard.pdf` for the full dashboard.

## Data
Raw data files are not included because of their size. Place the CSVs in a `data/` folder and run `ingestion_db.py`.
