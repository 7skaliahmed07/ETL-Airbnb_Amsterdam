import pandas as pd
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_imports():
    logger.info("Testing imports...")
    assert pd.__version__  
    assert requests.__version__
    logger.info("Imports successful!")

if __name__ == "__main__":
    test_imports()