import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

import seaborn as sns

# --- 1. Title and Description ---
st.title("The Importance of Handwashing")
st.markdown("""
This app explores the historical data from Dr. Ignaz Semmelweis, who discovered that 
**handwashing** significantly reduced mortality rates in maternity wards in the 1840s.
""")


# Replace 'your_file_name.csv' with the actual path to your CSV file
df = pd.read_csv('yearly_deaths_by_clinic-1.csv')

# --- 1. Title and Description ---
st.subheader("The Semmelweis Analysis: Handwashing and Mortality")
st.markdown("""
This app explores historical data from the clicnic (1841-1849). 
Dr. Ignaz Semmelweis noticed a horrifying difference in death rates between two clinics, 
leading to one of the most important medical discoveries in history. 
""")

# --- 2. Load Data ---
try:
    # Load Data
    df = pd.read_csv('yearly_deaths_by_clinic-1.csv')
    
    # Calculate death rate
    df['Death Rate (%)'] = (df['Deaths'] / df['Birth']) * 100

    # --- 3. Sidebar Filter ---
    st.sidebar.header("Filter Options")
    selected_clinic = st.sidebar.multiselect(
        "Select Clinics:",
        options=df['Clinic'].unique(),
        default=df['Clinic'].unique()
    )
    filtered_df = df[df['Clinic'].isin(selected_clinic)]

    # --- 4. Interactive Visualizations (Plotly) ---
    
    # Chart 1: Interactive Line Chart
    st.subheader("Annual Death Rate Trend")
    # px.line automatically includes tooltips
    fig1 = px.line(
        filtered_df, 
        x='Year', 
        y='Death Rate (%)', 
        color='Clinic',
        markers=True,
        hover_data={'Year': True, 'Death Rate (%)': ':.2f', 'Deaths': True},
        title="Death Rate Over Time"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: Interactive Bar Chart
    st.subheader("Births vs. Deaths Comparison")
    fig2 = px.bar(
        filtered_df, 
        x='Year', 
        y='Deaths', 
        color='Clinic',
        barmode='group',
        hover_data=['Birth', 'Deaths'],
        title="Number of Deaths per Year"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # --- 5. Findings ---
    st.divider()
    st.info("""
    **Findings:** By hovering over the data points, we can see the exact impact of the 1847 
    handwashing intervention. The tooltips show that while births remained high, the 
    number of deaths in Clinic 1 plummeted compared to previous years.
    The visualization clearly shows that Clinic 1 had a significantly higher average 
    death rate compared to Clinic 2. This discrepancy was the key observation that led Dr. Semmelweis 
    to investigate the differences in medical practices between the two wards.
    """)

except FileNotFoundError:
    st.error("CSV file not found. Check your GitHub repository for 'yearly_deaths_by_clinic-1.csv'.")
