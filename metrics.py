import streamlit as st
import pandas as pd

# Sample DataFrame with only numerical columns
data = {
    "Name": ["Alice", "Bob", "Charlie"], 
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]  # Added another numerical column
}
df = pd.DataFrame(data)

# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=["number"])

# Display numerical metrics
st.metric(label="Sum of Total Age", value=int(df["Age"].sum()))
st.metric(label="Mean of Total Age", value=round(df["Age"].mean(), 2))
st.metric(label="Max of Total Age", value=int(df["Age"].max()))
st.metric(label="Min of Total Age", value=int(df["Age"].min()))
st.metric(label="Count of Total Age", value=int(df["Age"].count()))
st.metric(label="Median of Total Age", value=int(df["Age"].median()))
st.metric(label="Standard Deviation of Total Age", value=round(df["Age"].std(), 2))
st.metric(label="Variance of Total Age", value=round(df["Age"].var(), 2))

# Fixed: Correlation requires two numerical columns
st.metric(label="Correlation of Age & Salary", value=round(df["Age"].corr(df["Salary"]), 2))

# Fixed: Convert Series outputs to a single value or string
st.metric(label="Mode of Total Age", value=str(df["Age"].mode().tolist()))
st.metric(label="Cumulative Sum of Total Age", value=str(df["Age"].cumsum().tolist()))
st.metric(label="Cumulative Product of Total Age", value=str(df["Age"].cumprod().tolist()))

# Fixed: Display correlation table with only numerical columns
st.write("### Correlation Table")
st.write(numeric_df.corr())
