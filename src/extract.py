import pandas as pd
import gzip
import logging
from pathlib import Path
import os

# Create logs directory if it doesn't exist
os.makedirs("./logs", exist_ok=True)

# Logging Setup
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("./logs/extract.log"),  # saves to logs/ folder
        logging.StreamHandler()                     # also prints to terminal
    ]
)
logger = logging.getLogger("AirbnbETL.Extract")


def load_gz_csv(file_path: str, sample: int = None) -> pd.DataFrame:
    """
    Load any .csv.gz file with full logging and debugging support
    """
    path = Path(file_path)
    if not path.exists():
        logger.error(f"File not found: {path}")
        raise FileNotFoundError(path)
    
    logger.info(f"Loading {path.name} ({path.stat().st_size / 1e6:.1f} MB compressed)")
    
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        df = pd.read_csv(f, nrows=sample, low_memory=False)
        logger.info(f"Successfully loaded {len(df):,} rows × {len(df.columns)} columns")
        logger.debug(f"Columns: {list(df.columns)}")
    
    return df

if __name__ == "__main__":
    # Quick test on the real listings file you just copied
    df = load_gz_csv("data/raw/listings.csv.gz", sample=1000)
    print("\nFirst 5 rows:")
    print(df.head())
    print(f"\nShape: {df.shape}")
    print(f"\nColumns ({len(df.columns)}): {list(df.columns)}")
