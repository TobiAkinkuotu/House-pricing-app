import streamlit as st
import numpy as np
import pickle

# Load the saved model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define locations and mapping
locations = ["Ikeja", "Lekki Phase I", "Banana Island", "Victoria Island"]
location_mapping = {loc: i for i, loc in enumerate(locations)}

# ------------------------
# Page configuration
# ------------------------
st.set_page_config(
    page_title="🏠 Emerald Homes",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ------------------------
# Custom CSS for colors
# ------------------------
st.markdown(
    """
    <style>
    /* Main background */
    .main {
        background-color: #FFFFFF;
    }
    
    /* Header */
    h1 {
        color: #1E90FF;  /* blue */
        text-align: center;
        font-family: 'Arial';
    }

    /* Prediction button */
    .stButton>button {
        background-color: #FF69B4;  /* pink */
        color: white;
        font-size: 16px;
        height: 50px;
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }

    /* Input boxes */
    div.stNumberInput>div>input {
        border: 2px solid #1E90FF;
        border-radius: 5px;
        padding: 5px;
    }

    /* Select box */
    div.stSelectbox>div>div>div {
        border: 2px solid #FF69B4;
        border-radius: 5px;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# App Title
# ------------------------
st.markdown("<h1>🏠 Emerald Homes</h1>", unsafe_allow_html=True)
st.write("---")

# ------------------------
# Inputs in columns
# ------------------------
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (Square Feet)", min_value=0)
    bhk = st.number_input("Number of Bedrooms", min_value=0)

with col2:
    bath = st.number_input("Number of Bathrooms", min_value=0)
    balcony = st.number_input("Number of Balconies", min_value=0)

# Location input (full width)
location = st.selectbox("Select Location", locations)

# ------------------------
# Prediction Button
# ------------------------
if st.button("🏡 Predict House Price"):
    # Encode location
    location_encoded = location_mapping[location]

    # Prepare features array
    features = np.array([[area, bhk, bath, balcony, location_encoded]])

    # Make prediction
    prediction = model.predict(features)
    st.success(f"Predicted House Price: $ {prediction[0]:,.2f}")
