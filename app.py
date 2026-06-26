import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load trained model
# -------------------------------
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# -------------------------------
# Streamlit page settings
# -------------------------------
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# -------------------------------
# App Title
# -------------------------------
st.title("🏠 House Price Prediction App")
st.write("Predict house prices using **square footage**, **bedrooms**, and **bathrooms**.")

st.markdown("---")

# -------------------------------
# User Inputs
# -------------------------------
st.subheader("Enter House Details")

sqft_living = st.number_input("Square Footage (sqft_living)", min_value=100, max_value=20000, value=2000, step=50)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=20, value=3, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1.0, max_value=20.0, value=2.0, step=0.5)

# -------------------------------
# Predict Button
# -------------------------------
if st.button("Predict House Price"):
    input_data = pd.DataFrame({
        'sqft_living': [sqft_living],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted House Price: ₹ {prediction:,.2f}")

# -------------------------------
# Show Input Data
# -------------------------------
st.markdown("---")
st.subheader("Input Summary")
st.write(f"**Square Footage:** {sqft_living}")
st.write(f"**Bedrooms:** {bedrooms}")
st.write(f"**Bathrooms:** {bathrooms}")