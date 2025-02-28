import streamlit as st 
import pandas as pd
import yfinance as yf 

#title
st.title("Sample Demo")

#headers and subheader
st.header("Welcome to streamlit")
st.subheader("streamlit for beginners")

#markdown
st.markdown("This is a markdown")


code_python = """
def add(a, b):
    return a + b
"""
st.code(code_python, language='python')

#divider
st.divider()

