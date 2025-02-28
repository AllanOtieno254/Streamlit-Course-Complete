import streamlit as st

# Define st.fragment if it doesn't exist
if not hasattr(st, "fragment"):
    def fragment(func):
        return func
    st.fragment = fragment

# Define st.toggle if it doesn't exist
if not hasattr(st, "toggle"):
    def toggle(label, key=None):
        # Fallback using checkbox to simulate toggle functionality
        return st.checkbox(label, key=key)
    st.toggle = toggle

st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    st.toggle("Show text")
    st.text_area("Enter your text")
    
@st.fragment()
def filter_and_file():
    st.checkbox("filter")
    st.file_uploader("Upload image")
    st.selectbox("choose option", ["option1", "option2", "option3"])
    st.slider("choose value", 0, 100, 50)
    st.text_input("Enter text")
    
# Render the fragments and other widgets vertically
toggle_and_text()

st.selectbox("select", (1, 2, 3), None)
st.button("update")

filter_and_file()
