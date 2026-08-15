from db import run_select


print("Testing database query...\n")


queries = [
    "SELECT COUNT(*) AS total_customers FROM customers",
    "SELECT COUNT(*) AS total_products FROM products",
    "SELECT COUNT(*) AS total_stores FROM stores",
    "SELECT COUNT(*) AS total_orders FROM sales_transactions",
    "SELECT COUNT(*) AS total_returns FROM returns",
]


for sql in queries:

    print("SQL:", sql)

    try:

        rows = run_select(sql)

        print("Result:", rows)

    except Exception as e:

        print("ERROR:", e)

    print("-" * 50)