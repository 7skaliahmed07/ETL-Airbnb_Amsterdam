import pandas as pd
from src.transform import clean_listings

def test_price_conversion():
    df = pd.DataFrame({"price": ["$150.00", "$99.50", None]})
    result = clean_listings(df)
    assert result['price'].dtype == float
    assert result['price'].iloc[0] == 150.0
    print("Test passed: price cleaned correctly")
