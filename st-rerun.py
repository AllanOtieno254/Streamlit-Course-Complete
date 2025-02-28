import streamlit as st

st.title("Counter example with immediate rerun")

if "count" not in st.session_state:
    st.session_state.count = 0

def increment_and_rerun():
    st.session_state.count += 1
    try:
        st.experimental_rerun()  # Attempt to immediately rerun the app
    except AttributeError:
        # Fallback for older Streamlit versions that don't support experimental_rerun
        st.write("Immediate rerun is not supported in your Streamlit version. Please update to the latest version for this feature.")

st.write(f"Current count: {st.session_state.count}")

if st.button("Increment and update immediately"):
    increment_and_rerun()
