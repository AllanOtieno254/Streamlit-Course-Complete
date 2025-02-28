import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt

st.write("Hello world")  
st.write(1234)  

st.write("Hello world",1234)

1234

import streamlit as st
import pandas as pd

import streamlit as st

# Function that returns a greeting message
def greet(name):
    return "Hello, " + name + "!"

# Call function and display output in Streamlit
st.write(greet("Allan"))


code_example="""
def greet(name):
    print("Hello", name)
"""
st.code(code_example, language='python')

import streamlit as st

code_python = """
def add(a, b):
    return a + b
"""
st.code(code_python, language='python')

code_html = """
<h1>Hello, World!</h1>
"""
st.code(code_html, language='html')

