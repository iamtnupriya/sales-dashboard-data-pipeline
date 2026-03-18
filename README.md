# Sales Dashboard Data Pipeline

An end-to-end data engineering project that extracts sales data from a CSV file, transforms it using Python and Pandas, loads it into PostgreSQL, and visualizes the results in Power BI.

## Project Overview

This project demonstrates a beginner-friendly ETL pipeline and dashboard workflow for sales analytics. It shows how raw sales data is collected, cleaned, stored in a database, and transformed into useful business insights through interactive visualizations.

## Tech Stack

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Power BI
- python-dotenv

## Project Workflow

1. Extract sales data from a CSV file
2. Transform the data using Pandas
3. Load cleaned data into PostgreSQL
4. Connect Power BI to PostgreSQL
5. Build interactive dashboard visuals

## Project Structure

```bash
sales-data-pipeline/
│
├── data/
│   ├── sales.csv
│   └── clean_sales.csv
│
├── dashboard/
│   └── sales_dashboard.pbix
│
├── myenv/
├── notebooks/
├── scripts/
│   └── etl.py
│
├── sql/
├── .env
├── .gitignore
├── README.md
└── requirements.txt