import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

connection_url = URL.create(
    drivername="mysql+pymysql",
    username=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=int(MYSQL_PORT),
    database=MYSQL_DATABASE,
)

engine = create_engine(connection_url)

files = {
    "customers": "customers.csv",
    "products": "products.csv",
    "stores": "stores.csv",
    "sales_transactions": "sales_transactions.csv",
    "returns": "returns.csv",
}

print("Starting data load...\n")

for table, filename in files.items():

    path = Path("data") / filename

    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    df = pd.read_csv(path)

    print(f"Loading {filename}...")
    print(f"Rows found: {len(df)}")

    # Insert into the existing MySQL table.
    # We use append because the tables already contain
    # the required schema and foreign keys.
    df.to_sql(
        table,
        engine,
        if_exists="append",
        index=False,
    )

    print(f"Loaded {len(df)} rows into {table}")
    print("-" * 50)


print("\nVerifying database row counts...\n")

with engine.connect() as conn:

    for table in files:

        count = conn.execute(
            text(f"SELECT COUNT(*) FROM `{table}`")
        ).scalar()

        print(f"{table}: {count} rows")

print("\nData loading completed successfully!")