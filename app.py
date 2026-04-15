import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Title and Description ---
st.title("The Importance of Handwashing")
st.markdown("""
This app explores the historical data from Dr. Ignaz Semmelweis, who discovered that 
**handwashing** significantly reduced mortality rates in maternity wards in the 1840s.
""")

# --- 2. Load Data ---
# Replace 'handwashing_data.csv' with your actual filename
@st.cache_data
def load_data():
    df = pd.read_csv("handwashing_data.csv")
    # Ensure date column is datetime format
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    return df

try:
    df = load_data()

    # --- 3. Optional: Filters ---
    if 'year' in df.columns:
        years = df['year'].unique()
        selected_year = st.sidebar.slider("Select Year Range", int(min(years)), int(max(years)), (int(min(years)), int(max(years))))
        df = df[(df['year'] >= selected_year[0]) & (df['year'] <= selected_year[1])]

    # --- 4. Visualizations ---
    st.subheader("Mortality Trends Over Time")
    
    fig, ax = plt.subplots()
    # Example: Plotting deaths or proportion of deaths
    ax.plot(df['date'], df['proportion_deaths'], label="Proportion of Deaths", color='red')
    
    # Optional: Highlight handwashing start (approx. 1847-06-01)
    # ax.axvline(pd.to_datetime('1847-06-01'), color='black', linestyle='--', label='Handwashing Begins')
    
    ax.set_ylabel("Proportion of Deaths")
    ax.legend()
    st.pyplot(fig)

    # --- 5. Findings ---
    st.info("""
    **Findings:** The data shows a sharp decline in the proportion of deaths immediately 
    following the introduction of mandatory handwashing. This visual evidence highlights 
    the critical impact of basic hygiene on patient survival rates.
    """)

except FileNotFoundError:
    st.error("Please ensure the dataset is in the same folder as this script!")