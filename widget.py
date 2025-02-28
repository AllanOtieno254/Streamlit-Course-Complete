import streamlit as st

st.button("ok")
st.button("ok", key="btn2")

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("set min value", 0, 50, 25)
st.session_state.slider = st.slider("slider", min_value, 100, min_value, st.session_state.slider)

# if a widget is nolonger rendered on the screen its state is destroyed 
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("show input field", value=st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
    user_input = st.text_input("Enter your name",value=st.session_state.get("user_input", ""))
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")
    st.write(f"Your name is {user_input}")
