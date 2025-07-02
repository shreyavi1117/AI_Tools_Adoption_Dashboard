import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('AI_Tools_Adoption_SMBs_India_Updated.csv')

st.title('📊 AI Tools Adoption in Indian SMBs - Dashboard')

# Show dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Sector-wise Distribution
st.subheader("Sector-wise Distribution")
sector_count = df['Sector'].value_counts()
st.bar_chart(sector_count)

# ROI vs Adoption Level
st.subheader("ROI vs AI Adoption Level")
fig, ax = plt.subplots()
sns.boxplot(data=df, x='Adoption_Level', y='ROI_Percentage', ax=ax)
st.pyplot(fig)

# AI Tools Used Wordcloud or List
st.subheader("Top AI Tools Used")
tools = df['AI_Tools_Used'].str.split(',').explode().str.strip().value_counts().head(10)
st.bar_chart(tools)

# Challenges Word Frequency (optional)
st.subheader("Common Challenges Faced")
challenges = df['Challenges'].str.split(',').explode().str.strip().value_counts().head(10)
st.bar_chart(challenges)
