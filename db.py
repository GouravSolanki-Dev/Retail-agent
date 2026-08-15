import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

from sql_safety import validate_sql


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


def run_select(sql: str, max_rows: int = 20):
    """
    Validate and execute a read-only SQL query.
    """

    safe_sql = validate_sql(sql)

    with engine.connect() as connection:

        result = connection.execute(text(safe_sql))

        rows = [
            dict(row._mapping)
            for row in result.fetchmany(max_rows)
        ]

    return rows