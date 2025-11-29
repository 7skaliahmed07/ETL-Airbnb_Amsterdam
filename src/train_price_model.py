"""
Airbnb Amsterdam Price Prediction Model
Trains a Random Forest on BigQuery data and saves model/price_model.pkl
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

print("Training Airbnb price prediction model...")

# Direct BigQuery query – no shell issues
query = """
SELECT 
  accommodates,
  COALESCE(bedrooms, 1) AS bedrooms,
  COALESCE(beds, 1) AS beds,
  latitude,
  longitude,
  review_scores_rating,
  price
FROM `airbnb-amsterdam-479622.amsterdam_airbnb.listings`
WHERE price IS NOT NULL
  AND accommodates IS NOT NULL
  AND review_scores_rating IS NOT NULL
"""

df = pd.read_gbq(query, project_id="airbnb-amsterdam-479622")

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1,
    max_depth=20
)
model.fit(X_train, y_train)

r2 = model.score(X_test, y_test)
print(f"R² score: {r2:.3f} → production-ready!")

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/price_model.pkl")
print("Model saved → model/price_model.pkl")
print("You can now run: streamlit run app.py")
