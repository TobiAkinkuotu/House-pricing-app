import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("🏠 House Price Prediction App")

area = st.number_input("Area (Square Feet)", min_value=0)
bhk = st.number_input("Number of Bedrooms", min_value=0)
bath = st.number_input("Number of Bathrooms", min_value=0)
balcony = st.number_input("Number of Balconies", min_value=0)

if st.button("Predict Price"):
    features = np.array([[area, bhk, bath, balcony]])
    prediction = model.predict(features)
    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")
