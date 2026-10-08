import os
import time
import logging
import pandas as pd
from sqlalchemy import create_engine

# Create the logs folder if it does not exist
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

# SQLite database connection (creates inventory.db if it does not exist)
engine = create_engine('sqlite:///inventory.db')

# Number of rows to read at a time
CHUNK_SIZE = 100_000


def ingest_db(df, table_name, engine, if_exists='append'):
    """Writes a DataFrame into a database table."""
    df.to_sql(
        table_name,
        con=engine,
        if_exists=if_exists,
        index=False,
        chunksize=10000
    )


def load_raw_data():
    """Reads every CSV in data/ in chunks and loads it into the database."""
    start = time.time()

    for file in os.listdir('data'):
        if file.endswith('.csv'):
            table_name = file[:-4]
            path = os.path.join('data', file)
            first_chunk = True

            logging.info(f'Ingesting {file}')

            for chunk in pd.read_csv(path, chunksize=CHUNK_SIZE):
                # First chunk replaces the old table, the rest are appended
                ingest_db(
                    chunk,
                    table_name,
                    engine,
                    if_exists='replace' if first_chunk else 'append'
                )
                first_chunk = False

            logging.info(f'Finished {file}')

    total_time = (time.time() - start) / 60
    logging.info(f'Ingestion complete. Total time: {total_time:.2f} minutes')


if __name__ == '__main__':
    load_raw_data()