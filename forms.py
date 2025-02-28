import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Form Demo")

# Form to hold interactive elements
with st.form(key="sample_form"):
    
    # Text input
    st.subheader("Text Input")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Enter your feedback")
    
    # Date and Time input
    st.subheader("Date and Time Input")
    dob = st.date_input("Enter your date of birth")
    time = st.time_input("Enter the time")
    
    # Selectors
    st.subheader("Selectors")  
    choice = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    slide_value = st.select_slider("Select a value", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    # Toggles and checkboxes
    st.subheader("Toggles and Checkboxes")
    notification = st.checkbox("Enable notifications")
    toggle_value = st.checkbox("Enable dark mode?", value=False)
    
    # Submit button for the form
    submit_button = st.form_submit_button(label="Submit")
    print("pressed",submit_button)

# Outside of the form
st.subheader("Buttons")
if st.button("Click me"):
    st.write(f"Hello",name)
    
    
    
    
    