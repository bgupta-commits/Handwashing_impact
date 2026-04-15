import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Title and Description ---
st.title("The Importance of Handwashing")
st.markdown("""
This app explores the historical data from Dr. Ignaz Semmelweis, who discovered that 
**handwashing** significantly reduced mortality rates in maternity wards in the 1840s.
""")


# Replace 'your_file_name.csv' with the actual path to your CSV file
df = pd.read_csv('yearly_deaths_by_clinic-1.csv')

display(df)
