import streamlit as st

# A simple counter variable with session state

if "counter" not in st.session_state:
    st.session_state.counter = 0  # Fixed assignment operator

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}") 

if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write(f"Counter value: {st.session_state.counter}")
