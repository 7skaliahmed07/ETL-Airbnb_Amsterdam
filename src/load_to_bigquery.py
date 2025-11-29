from google.cloud import bigquery
import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BigQueryLoad")

client = bigquery.Client(project='airbnb-amsterdam-479622')
dataset_id = f"{client.project}.amsterdam_airbnb"

def load_df_to_bq(df: pd.DataFrame, table_name: str):
    table_id = f"{dataset_id}.{table_name}"
    job = client.load_table_from_dataframe(df, table_id)
    job.result()  # wait for completion
    logger.info(f"Loaded {len(df):,} rows → BigQuery table {table_name}")

if __name__ == "__main__":
    from extract import load_gz_csv
    from transform import clean_listings, clean_calendar, clean_reviews
    
    load_df_to_bq(clean_listings(load_gz_csv("data/raw/listings.csv.gz")), "listings")
    load_df_to_bq(clean_calendar(load_gz_csv("data/raw/calendar.csv.gz")), "calendar")
    load_df_to_bq(clean_reviews(load_gz_csv("data/raw/reviews.csv.gz")),  "reviews")
    print("All data is now in Google Cloud BigQuery!")
