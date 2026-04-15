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
