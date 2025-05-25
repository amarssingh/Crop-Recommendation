import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load model and scaler
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('minmaxscaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Crop label to name mapping
crop_map = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}


st.set_page_config(page_title="Crop Prediction", layout="centered")

st.title("🌱 Crop Recommendation System")
st.write("Provide soil and climate information to get the best crop recommendation.")

# Input fields
N = st.number_input("Nitrogen (N)", 0.0, 140.0, step=1.0)
P = st.number_input("Phosphorus (P)", 5.0, 145.0, step=1.0)
K = st.number_input("Potassium (K)", 5.0, 205.0, step=1.0)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0)
humidity = st.number_input("Humidity (%)", 10.0, 100.0)
ph = st.number_input("Soil pH", 3.5, 9.5)
rainfall = st.number_input("Rainfall (mm)", 20.0, 300.0)

if st.button("Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    crop_name = crop_map.get(prediction[0], "Unknown Crop")
    st.success(f"🌾 Recommended Crop: **{crop_name}**")
