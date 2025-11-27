import streamlit as st
import numpy as np
from joblib import load

# ------------------------
# Load the saved model
# ------------------------
model = load("housing_model.joblib")

# ------------------------
# Page configuration
# ------------------------
st.set_page_config(
    page_title="🏡 Emerald Homes Price Predictor",
    page_icon="🏡",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.sidebar.header("🧑‍🤝‍🧑 Team Members")
st.sidebar.markdown("**Team Members**")
members_data = [
    "1. Akinkuotu Oluwatobiloba Daniel",
    "2. Adeyinka Oluwaseyi Emmanuel",
    "3. Aneke Ester Chiamaka",
    "4. Ezeh Vanessa Adaugo",
    "5. Oyelade Temilola Oyewale",
    "6. Odeh Samuel Adi",
    "7. Anamah Nnamdi Prince",
    "8. Aderinto Ayomide Peter",
    "9. Amagwu Munachimso Alma",
    "10. Afolabi Oluwadarasimi Gabriel",
    "11. Adekunle Adeoba Samuel"
    ]
for member in members_data:
    st.sidebar.write(member.upper())
# ------------------------
# Custom CSS Styling
# ------------------------
st.markdown(
    """
    <style>
    /* Main background */
    .main {
        background-color: #F5F7FA;
    }
    
    /* Title styling */
    h1 {
        color: #1E3A8A;  /* deep blue */
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: 700;
    }

    /* Input boxes styling */
    div.stNumberInput>div>input {
        border: 2px solid #1E3A8A;
        border-radius: 8px;
        padding: 8px;
        font-size: 16px;
    }

    /* Prediction button */
    div.stButton>button {
        background: linear-gradient(90deg, #FF6EC7, #FF3CAC);
        color: white;
        font-size: 18px;
        font-weight: bold;
        height: 50px;
        width: 100%;
        border-radius: 12px;
        transition: 0.3s;
    }

    div.stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }

    /* Price output box */
    .price-output {
        font-size: 28px;
        font-weight: 700;
        color: #FF3CAC;
        text-align: center;
        animation: pop 0.8s ease-out;
    }

    /* Animation */
    @keyframes pop {
        0% { transform: scale(0.5); opacity: 0; }
        70% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# App Title
# ------------------------
st.markdown("<h1>🏡 Emerald Homes Price Predictor</h1>", unsafe_allow_html=True)
st.write("Enter the details of your property below to predict its market price.")
st.write("---")

# ------------------------
# Input Columns
# ------------------------
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("🏠 Area (sq. ft.)", min_value=0)
    bhk = st.number_input("🛏 Bedrooms", min_value=0)

with col2:
    bath = st.number_input("🛁 Bathrooms", min_value=0)
    stories = st.number_input("🏢 Stories", min_value=0)
    parking = st.number_input("🚗 Parking Spaces", min_value=0)

# ------------------------
# Prediction Button
# ------------------------
if st.button("💰 Predict Price"):
    # Prepare features
    features = np.array([[area, bhk, bath, stories, parking]])
    
    # Predict price
    prediction_log = model.predict(features)
    prediction = np.expm1(prediction_log)
    
    # Display prediction with styled container
    st.markdown(
        f"<div class='price-output'>Estimated Price: 💵 {prediction[0]:,.2f}</div>",
        unsafe_allow_html=True
    )

    # Optional celebratory animation
    st.balloons()