import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load('cpu_performance_model.joblib')

# --- Web App Title and Description ---
st.title('Pre-Silicon CPU Performance Simulator')
st.write("""
This app simulates the performance of a CPU design based on key architectural parameters.
Adjust the sliders to see the model's prediction for the final performance score.
""")

# --- Create sliders for user input in the sidebar ---
st.sidebar.header('CPU Design Parameters')

at = st.sidebar.slider('Core Temperature (AT)', min_value=1.0, max_value=38.0, value=19.65, step=0.1)
v = st.sidebar.slider('L3 Cache Size (V)', min_value=25.0, max_value=82.0, value=54.3, step=0.1)
ap = st.sidebar.slider('Core Voltage (AP)', min_value=990.0, max_value=1035.0, value=1013.25, step=0.1)
rh = st.sidebar.slider('Memory Bus Speed (RH)', min_value=25.0, max_value=100.0, value=73.3, step=0.1)

# --- Make a prediction ---
# Put the inputs into a numpy array
input_data = np.array([[at, v, ap, rh]])

# Get the prediction from the model
prediction = model.predict(input_data)

# --- Display the result ---
st.header(f'Predicted Performance Score (PE):')
st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>{prediction[0]:.2f}</h1>", unsafe_allow_html=True)