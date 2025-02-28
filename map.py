import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Map")

# Generate random latitude and longitude points near San Francisco
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],  # Proper broadcasting
    columns=["lat", "lon"]  # Correct column definition
)

# Display map
st.map(map_data)
