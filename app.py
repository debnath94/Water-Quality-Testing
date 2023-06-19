# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:46:17 2023

@author: debna
"""

import streamlit as st
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Load the trained model from the pickled file
with open('water_quality_dt.pickle', 'rb') as file:
    model = pickle. load(file)

st.title("Water Quality Predictions")

# Create input fields for user input
temperature = st.number_input("Temperature (°C)")
turbidity = st.number_input("Turbidity (NTU)")
dissolved_oxygen = st.number_input("Dissolved Oxygen (mg/L)")
conductivity = st.number_input("Conductivity (µS/cm)")

if st. button("Predict"):
    query_point = np. array([temperature, turbidity, dissolved_oxygen, conductivity])
    query_point = query_point. reshape(1, -1)
    prediction = model.predict(query_point)
    st.write("The predicted PH value is", prediction[0])
    
# Perform actions based on the predicted pH value
    if prediction[0] < 7:
        st.subheader("Prediction is less than 7")
        st.write("Water is unhealthy")
    elif prediction[0] > 7:
        st.subheader("Prediction is greater than 7")
        st.write("water is healthy")
    else:
        st.subheader("Prediction is equal to 7")
        st.write("water is healthy to drink")




















