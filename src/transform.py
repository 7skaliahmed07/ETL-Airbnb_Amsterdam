import pandas as pd
import logging
from pathlib import Path
import numpy as np

logger = logging.getLogger("AirbnbETL.Transform")

def clean_listings(df: pd.DataFrame) -> pd.DataFrame:
    logger.info(f"Starting listings transformation – {len(df):,} rows")
    
    # Price: "$150.00" → 150.0
    if 'price' in df.columns:
        df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    
    # Percentage columns (host_response_rate, host_acceptance_rate)
    for col in ['host_response_rate', 'host_acceptance_rate']:
        if col in df.columns:
            df[col] = df[col].replace('%', '', regex=True).astype(float) / 100.0
    
    # Boolean columns
    bool_cols = ['host_is_superhost', 'host_has_profile_pic', 
                 'host_identity_verified', 'instant_bookable', 'has_availability']
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].map({'t': True, 'f': False, np.nan: False})
    
    # Dates
    date_cols = ['host_since', 'first_review', 'last_review']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    
    logger.info("Listings transformation completed")
    return df

def clean_calendar(df: pd.DataFrame) -> pd.DataFrame:
    logger.info(f"Cleaning calendar – {len(df):,} rows")
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['available'] = df['available'].map({'t': True, 'f': False})
    return df

def clean_reviews(df: pd.DataFrame) -> pd.DataFrame:
    logger.info(f"Cleaning reviews – {len(df):,} rows")
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df
