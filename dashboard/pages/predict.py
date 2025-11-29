import streamlit as st
import joblib
import pandas as pd
import os
import joblib

def load_model():
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base,"..","..","model","price_model.pkl")
    return joblib.load(path)

def show():
    st.header("AI Price Predictor")
    st.write("Predict nightly price using our trained Random Forest model")
    
    col1, col2 = st.columns(2)
    with col1:
        guests = st.slider("Guests", 1, 16, 4)
        beds = st.slider("Beds", 1, 20, 2)
        bedrooms = st.slider("Bedrooms", 0, 10, 2)
    with col2:
        rating = st.slider("Expected Rating", 3.0, 5.0, 4.8, 0.1)
        neighbourhood = st.selectbox("Neighbourhood", 
            ["De Pijp", "Centrum", "Jordaan", "Oud-West", "Zuid"])
    
    if st.button("Predict Price", type="primary"):
        # model = joblib.load("model/price_model.pkl")
        model = load_model()
        # Use median lat/lon averages
        coords = {"De Pijp": (52.35, 4.90), "Centrum": (52.37, 4.89), 
                  "Jordaan": (52.38, 4.88), "Oud-West": (52.37, 4.87), "Zuid": (52.35, 4.88)}
        lat, lon = coords[neighbourhood]
        
        pred = model.predict([[guests, bedrooms, beds, lat, lon, rating]])[0]
        st.success(f"Predicted Price: **€{pred:.0f} € per night**")
        st.balloons()
