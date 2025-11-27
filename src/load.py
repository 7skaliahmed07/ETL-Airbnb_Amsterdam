import sqlite3
import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger("AirbnbETL.Load")

def create_connection(db_path: str = "data/warehouse.db"):
    Path(db_path).parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(db_path)
    logger.info(f"Connected to SQLite database: {db_path}")
    return conn

def load_to_sqlite(df: pd.DataFrame, table_name: str, conn: sqlite3.Connection):
    logger.info(f"Loading {len(df):,} rows into table '{table_name}'")
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    # Create indexes for common queries (exactly what companies do)
    cursor = conn.cursor()
    if table_name == "listings":
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_neighbourhood ON listings(neighbourhood_cleansed)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_price ON listings(price)")
    conn.commit()
    logger.info(f"Table '{table_name}' loaded and indexed successfully")
