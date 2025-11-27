import logging
from pathlib import Path
from extract import load_gz_csv
from transform import clean_listings
from load import create_connection, load_to_sqlite

# Master logging config (used by all modules)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
)

def run_full_pipeline():
    logging.info("Starting Airbnb Amsterdam ETL Pipeline")
    
    # Extract
    listings_df = load_gz_csv("data/raw/listings.csv.gz")         
    calendar_df = load_gz_csv("data/raw/calendar.csv.gz")
    reviews_df  = load_gz_csv("data/raw/reviews.csv.gz")
    
    # Transform
    listings_clean = clean_listings(listings_df)
    
    # Load
    conn = create_connection()
    load_to_sqlite(listings_clean, "listings", conn)
    load_to_sqlite(calendar_df,   "calendar", conn)
    load_to_sqlite(reviews_df,    "reviews",  conn)
    
    conn.close()
    logging.info("Pipeline completed successfully!")

if __name__ == "__main__":
    run_full_pipeline()
