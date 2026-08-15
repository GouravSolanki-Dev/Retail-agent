from sql_safety import validate_sql


tests = [
    "SELECT * FROM customers",
    "SELECT COUNT(*) FROM sales_transactions",
    "DELETE FROM customers",
    "DROP TABLE customers",
    "UPDATE customers SET city = 'Delhi'",
    "INSERT INTO customers VALUES ('C999')",
]


for sql in tests:

    print("\nTesting:", sql)

    try:
        safe_sql = validate_sql(sql)
        print("ALLOWED:", safe_sql)

    except ValueError as e:
        print("BLOCKED:", e)