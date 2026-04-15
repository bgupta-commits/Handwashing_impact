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
st.dataframe(df)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Data Processing (Assisted by Gemini AI) ---
# Calculate death rate (deaths per 100 births)
df['death_rate'] = (df['Deaths'] / df['Birth']) * 100

# Group by clinic and calculate the mean death rate
clinic_death_rate = df.groupby('Clinic')['death_rate'].mean().reset_index()

# --- Create the Visualization ---
st.subheader("Average Death Rate by Clinic")

# Create the figure object explicitly
fig, ax = plt.subplots(figsize=(8, 6))

sns.barplot(
    x='Clinic', 
    y='death_rate', 
    hue='Clinic', 
    data=clinic_death_rate, 
    palette='viridis', 
    legend=False,
    ax=ax  # Tell seaborn to use the 'ax' we just created
)

ax.set_title('Average Death Rate by Clinic (per 100 Births)')
ax.set_xlabel('Clinic')
ax.set_ylabel('Average Death Rate (%)')
ax.set_ylim(0, clinic_death_rate['death_rate'].max() * 1.1)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# --- Display the plot in Streamlit ---
st.pyplot(fig) 

# --- Short Explanation (Required for your assignment) ---
st.write("""
**Findings:** The visualization clearly shows that Clinic 1 had a significantly higher average 
death rate compared to Clinic 2. This discrepancy was the key observation that led Dr. Semmelweis 
to investigate the differences in medical practices between the two wards.
""")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Title and Description ---
st.title("The Semmelweis Analysis: Handwashing and Mortality")
st.markdown("""
This app explores historical data from the Vienna General Hospital (1841-1849). 
Dr. Ignaz Semmelweis noticed a horrifying difference in death rates between two clinics, 
leading to one of the most important medical discoveries in history.
""")

# --- 2. Load Data ---
# Code snippet assisted by Gemini AI
try:
    df = pd.read_csv('yearly_deaths_by_clinic-1.csv')
    
    # Calculate death rate (Percentage of deaths per birth)
    df['Death Rate (%)'] = (df['Deaths'] / df['Birth']) * 100

    # --- 3. Optional Filter (Assignment Requirement) ---
    st.sidebar.header("Filter Options")
    selected_clinic = st.sidebar.multiselect(
        "Select Clinics to Compare:",
        options=df['Clinic'].unique(),
        default=df['Clinic'].unique()
    )
    
    # Filter the dataframe based on selection
    filtered_df = df[df['Clinic'].isin(selected_clinic)]

    # --- 4. Visualizations ---
    
    # Chart 1: Line Chart showing Trends over Time
    st.subheader("Mortality Rates Over the Years")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=filtered_df, x='Year', y='Death Rate (%)', hue='Clinic', marker='o', ax=ax1)
    ax1.set_title("Annual Death Rate Trend by Clinic")
    st.pyplot(fig1)

    # Chart 2: Bar Chart showing Total Deaths vs Births
    st.subheader("Total Births vs. Total Deaths")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    # Comparison of raw numbers
    clinic_totals = filtered_df.groupby('Clinic')[['Birth', 'Deaths']].sum().reset_index()
    clinic_totals_melted = clinic_totals.melt(id_vars='Clinic', var_name='Type', value_name='Count')
    sns.barplot(data=clinic_totals_melted, x='Clinic', y='Count', hue='Type', ax=ax2)
    st.pyplot(fig2)

    # --- 5. Short Explanation of Findings (Assignment Requirement) ---
    st.divider()
    st.subheader("Analysis Findings")
    st.write("""
    The visualizations indicate that **clinic 1** consistently had a much higher death rate 
    than **clinic 2** during the early 1840s. A sharp decline is visible in the later years 
    for clinic 1, which corresponds historically to the introduction of mandatory hand-washing 
    with chlorinated lime solutions.
    """)

except FileNotFoundError:
    st.error("CSV file not found. Ensure 'yearly_deaths_by_clinic-1.csv' is in your GitHub repository.")


import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. Title and Description ---
st.title("The Semmelweis Analysis: Handwashing and Mortality")
st.markdown("""
Hover over the charts below to see the exact numbers for births, deaths, and mortality rates.
""")

# --- 2. Load Data ---
try:
    # Code snippet assisted by Gemini AI
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
    """)

except FileNotFoundError:
    st.error("CSV file not found. Check your GitHub repository for 'yearly_deaths_by_clinic-1.csv'.")
