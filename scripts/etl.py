import pandas as pd
import sqlalchemy 

# =========================
# EXTRACT
# =========================
df = pd.read_csv("data/sales.csv")

print("\n Raw Data:")
print(df.head())

# =========================
# TRANSFORM
# =========================

# 1. Remove duplicates
df.drop_duplicates(inplace=True)

# 2. Handle missing values
df.dropna(inplace=True)

# 3. Convert date column
df['date'] = pd.to_datetime(df['date'])

# 4. Feature Engineering
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# 5. Standardize column names
df.columns = [col.lower() for col in df.columns]

# 6. Sort data
df.sort_values(by='date', inplace=True)

print("\n Cleaned Data:")
print(df.head())


# Revenue per category
category_sales = df.groupby('category')['amount'].sum()
print("\nSales by Category:")
print(category_sales)



# =========================
# SAVE CLEAN DATA (Optional)
# =========================
df.to_csv("data/clean_sales.csv", index=False)

print("\n Transformation Completed & Saved!")


# =========================
# LOAD (PostgreSQL)
# =========================

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

# Create DB connection
engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

# Load data into PostgreSQL
df.to_sql("sales", engine, if_exists="replace", index=False)

print("\nData loaded into PostgreSQL successfully!")