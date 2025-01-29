"""
Usage:
pip install -r requirements.txt
python -m pip install -U pip
./venv.ps1
python db.py
"""

from os import remove
from os.path import exists
from pandas import DataFrame
from pathlib import Path
from sqlalchemy import Connection, CursorResult, Engine, create_engine, text
from typing import Any


def main() -> None:
    # Path to the SQLite database file
    database_path: Path = Path(__file__).parent.joinpath("database.sqlite")

    # Get the connection to the database
    connection: Connection = connect(database_path)

    # Create or replace the table
    create_table(connection)

    # Insert records into the table
    insert_records(connection)

    # Select records from the table
    contain: str = "e"
    data_frame: DataFrame = select_records(connection, contain)

    # Disconnect from thedatabase
    disconnect(connection)

    # Delete the database file
    delete(database_path)

    # Print the data frame
    print_data_frame(data_frame)
    

def connect(database_path: Path) -> Connection:
    # Create the SQLAlchemy engine
    url: str = f"sqlite:///{database_path}"
    engine: Engine = create_engine(url)

    # Connect to the database
    connection: Connection = engine.connect()

    return connection


def create_table(connection: Connection, table: str = "test_table") -> None:
    sql: str = f"""CREATE TABLE IF NOT EXISTS {table} (
    id INTEGER PRIMARY KEY
    , name TEXT
)
;"""
    connection.execute(text(sql))


def insert_records(connection: Connection, table: str = "test_table") -> None:
    sql: str = f"""INSERT INTO {table} (name)
VALUES ('apple')
    , ('banana')
    , ('cherry')
    , ('date')
    , ('elderberry')
    , ('fig')
    , ('grape')
    , ('honeydew')
    , ('imbe')
    , ('jackfruit')
;"""
    connection.execute(text(sql))


def select_records(connection: Connection, contain: str, table: str = "test_table") -> DataFrame:
    sql: str = f"""SELECT * FROM {table}
WHERE name LIKE '%{contain}%'
ORDER BY name ASC
;"""
    cursor_result: CursorResult[Any] = connection.execute(text(sql))
    data_frame: DataFrame = DataFrame(cursor_result.fetchall(), columns=cursor_result.keys())

    return data_frame


def disconnect(connection: Connection) -> None:
    # Disconnect from the database
    connection.close()
    connection.engine.dispose()


def delete(path: Path) -> None:
    if exists(path):
        remove(path)


def print_data_frame(data_frame: DataFrame) -> None:
    print(data_frame.to_json(orient="records", indent=2))


if __name__ == "__main__":
    main()

