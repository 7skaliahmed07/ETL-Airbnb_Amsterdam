import streamlit as st
import tempfile
import json
import os

# Load service account from Streamlit secrets
sa_info = dict(st.secrets["SERVICE_ACCOUNT_JSON"])

# Write to temporary file
with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
    json.dump(sa_info, f)
    key_file = f.name

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file

# --- Now the rest of your imports ---
st.set_page_config(
    page_title="Amsterdam Airbnb Intelligence",
    page_icon="house",
    layout="wide",
    initial_sidebar_state="expanded"
)

import pandas as pd
import plotly.express as px
import joblib
from pages import home, explore, predict

# Custom CSS
st.markdown("""
<style>
    .big-font {font-size:50px !important; font-weight:bold; color:#FF5A5F;}
    .metric-card {background-color:#f0f2f6; padding:20px; border-radius:10px; text-align:center;}
    .stButton>button {background-color:#FF5A5F; color:white; border-radius:8px; height:50px; width:100%;}
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Amsterdam Airbnb Intelligence")
page = st.sidebar.radio("Go to", ["Home", "Explore Data", "Price Predictor"])

if page == "Home":
    home.show()
elif page == "Explore Data":
    explore.show()
else:
    predict.show()
