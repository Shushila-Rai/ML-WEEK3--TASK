import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
import joblib


model_path = os.path.join(os.getcwd(), 'notebook', 'models', 'linear_regression_model.pkl')
scaler_path = os.path.join(os.getcwd(), 'notebook', 'models', 'data_scaler.pkl')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


df = pd.read_csv('F:\ML Internship\ML Week3-Task\data\housing.csv') # Yahan apni dataset file ka naam likhein

st.title("🏡 California Housing Analysis & Prediction")

tab1, tab2, tab3 = st.tabs(["📊 Cleaned Dataset", "📈 Model Performance", "🔮 Price Prediction"])

with tab1:
    st.subheader("Cleaned Dataset Overview")
    st.write(df.head(10)) 
    st.write(f"Shape of Data: {df.shape}")

with tab2:
    st.subheader("Model Performance Visualization")
    st.image('notebook\Screenshots\output.png')

with tab3:
    st.subheader("House Price Prediction System")
  
    col1, col2 = st.columns(2)
    with col1:
        longitude = st.number_input("Longitude", -125.0, -114.0, -119.0)
        latitude = st.number_input("Latitude", 32.0, 42.0, 35.0)
        rooms = st.number_input("Total Rooms", 1, 39000, 2000)
    with col2:
        pop = st.number_input("Population", 3, 35000, 1500)
        income = st.number_input("Median Income", 0.5, 15.0, 3.5)
        proximity = st.selectbox("Ocean Proximity (Encoded)", [0, 1, 2, 3, 4])

    if st.button("Get Prediction"):
        input_data = np.array([[longitude, latitude, 28.0, rooms, pop, income, proximity]])
        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)
        st.success(f"The estimated house price is: ${prediction[0]:,.2f}")

