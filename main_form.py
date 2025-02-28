import streamlit as st
from datetime import datetime


# Title
st.title("Streamlit Form Demo")

# Form to hold interactive elements
#dictionalry
form_values={
    "name":None,
    "Height":None,
    "Gender":None,
    "dob":None
}

min_date=datetime(1900,1,1)
max_date=datetime.now()

with st.form(key="sample_form"):
    
    # Text input
    st.subheader("credentials")
    form_values["name"] = st.text_input("Enter your name")
    form_values["Height"] = st.number_input("Enter your Height")
    form_values["Gender"] = st.selectbox("Enter your Gender",["Male","Female","Other"])
    form_values["dob"] = st.date_input("Enter your date of birth",min_value=min_date,max_value=max_date)    
    
    submit_btn=st.form_submit_button(label="Submit")
    print("pressed",submit_btn)
    
    if submit_btn:
        if not all(form_values.values()):
            st.warning("Please fill all the fields")
        else:
                st.success("Form submitted successfully")
                st.balloons()
                st.write(form_values)
                for (key,value) in form_values.items():
                    st.write(f"{key}:{value}")
