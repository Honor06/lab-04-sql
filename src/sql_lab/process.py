import os
import pandas as pd
from sqlalchemy import create_engine
import logging
logging.basicConfig(level=logging.INFO)

DB_HOST = os.environ.get(
    "DB_HOST",
    "ds2022.cgls84scuy1e.us-east-1.rds.amazonaws.com"
)
DB_HOST = os.environ.get("DBHOST")
DB_NAME = os.environ.get("DBNAME")
DB_USER = os.environ.get("DBUSER")
DB_PASSWORD = os.environ.get("DBPASS")
CSV_FILE = "MOCK_DATA.csv"
TABLE = "mock"


def read_data(filename):
    """Loads a CSV file and returns a DataFrame."""
    logging.info("Reading data from CSV file")
    df = pd.read_csv(filename)
    logging.info("Data successfully read")
    return df

def clean_data(data):
    """Prepares a df for upload by removing rows with missing values."""
    cleaned_data = data.dropna().copy()
    logging.info("Data successfully cleaned")
    return cleaned_data

def load_data(data, table="mock"):
    """Writes the DataFrame to MySQL."""
    table = "mock"

    engine = create_engine(
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

    data.to_sql(
        name=table,
        con=engine,
        if_exists="append",
        index=False
    )

    logging.info("Data successfully loaded into MySQL")

def main():
    """Using all of the defined functions together."""
    data = read_data(CSV_FILE)
    data = clean_data(data)
    load_data(data, TABLE)
    logging.info("Data pipeline completed")


if __name__ == "__main__":
    main()