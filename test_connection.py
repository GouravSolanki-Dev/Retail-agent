import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()

host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
database = os.getenv("MYSQL_DATABASE")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")

print("Host:", host)
print("Port:", port)
print("Database:", database)
print("User:", user)
print("Password: [hidden]")


connection_url = URL.create(
    drivername="mysql+pymysql",
    username=user,
    password=password,
    host=host,
    port=int(port),
    database=database,
)

engine = create_engine(connection_url)



try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("\nMySQL connection successful!")
        print("Test result:", result.scalar())

except Exception as e:
    print("\nMySQL connection failed.")
    print("Error:", e)