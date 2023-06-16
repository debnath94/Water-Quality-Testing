# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:46:17 2023

@author: debna
"""

import streamlit as st
import pickle
import pandas as pd

# Load the trained model from the pickled file
with open('water_quality_dt.pickle', 'rb') as file:
    model = pickle. load(file)

# Create a function to preprocess the input data
def preprocess_input(data):
    # Preprocess the input data as needed
    # For example, you can convert the input to a DataFrame or perform feature engineering
    # Here, we assume the input is already in a DataFrame format
    processed_data = data.copy()
    return processed_data

# Create a function to make predictions

def make_prediction(model, input_data):
    #preprocess the input data
    preprocessed_input = preprocess_input(input_data)
    #make prediction
    predictions = model. predict(preprocessed_input)
    return predictions

# Create the Streamlit web application
def main():
    st.title("Water Quality Testing")

    # Create input fields for user input
    temperature = st.number_input("Temperature (°C)")
    turbidity = st.number_input("Turbidity (NTU)")
    dissolved_oxygen = st.number_input("Dissolved Oxygen (mg/L)")
    conductivity = st.number_input("Conductivity (µS/cm)")

# Create a dictionary with the input data
    input_data = {
        "Temperature_(°C)": temperature,
        "Turbidity_NTU": turbidity,
        "Dissolved Oxygen_mg/L": dissolved_oxygen,
        "Conductivity_µS/cm": conductivity
    }

# Convert the input data to a DataFrame
    input_df = pd.DataFrame(input_data, index=[0])

    # Make predictions using the model
    predictions = make_prediction(model, input_df)

    # Display the predicted pH value
    st.subheader("Predicted pH value")
    st.write(predictions[0])

# Perform actions based on the predicted pH value
    if predictions[0] < 7:
        st.subheader("Prediction is less than 7")
        st.write("Water is unhealthy")
    elif predictions[0] > 7:
        st.subheader("Prediction is greater than 7")
        st.write("water is healthy")
    else:
        st.subheader("Prediction is equal to 7")
        st.write("water is healthy to drink")

# Run the Streamlit web application
if __name__ == '__main__':
    main()



















