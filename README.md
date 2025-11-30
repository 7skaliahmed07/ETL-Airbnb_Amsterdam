<div align="center">
  <!-- <img src="https://raw.githubusercontent.com/yourusername/your-repo/main/dashboard/assets/architecture.png" width="100%"> -->
  <h1>Amsterdam Airbnb Intelligence Platform</h1>
  <p><b>End-to-end modern data stack • 10k+ listings • 3.8M rows • ML price prediction • Live dashboard</b></p>

[![Streamlit App](https://github.com/7skaliahmed07/ETL-Airbnb_Amsterdam/blob/44ed71a8acc7da3d09d37068936c439c5c684fdd/overview.jpg)

</div>

## Live Demo
[https://amsterdam-airbnb-intelligence.streamlit.app](https://etl-airbnbamsterdam-etl-pipeline-by-uzair.streamlit.app/)

## Tech Stack (Exactly what Dutch companies in Netherlands use)
- **Data Source**: Inside Airbnb (public)
- **Storage**: Google BigQuery (EU region, free tier)
- **ETL**: Python + Pandas + Logging + Modular code
- **ML**: Scikit-learn Random Forest (R² ≈ 0.73)
- **Dashboard**: Streamlit multi-page + Plotly + Custom CSS
- **Version Control**: Git + clean structure
- 
project/
├── data/
│   └── raw/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load_to_bigquery.py
│   └── train_price_model.py
├── model/
│   └── price_model.pkl
├── dashboard/
│   ├── app.py
│   └── pages/
├── requirements.txt




## Architecture (1 sentence)
Raw Airbnb CSVs → Python ETL → Google BigQuery → Train ML model → Multi-page Streamlit dashboard with live predictions

Made with love in 2025 | Ready for HSM-sponsored roles in Amsterdam
