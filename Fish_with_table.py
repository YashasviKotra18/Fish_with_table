import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('Fish.csv')

Fig1 = px.bar(df, x= 'Species', y = 'Weight', title = 'Bar plot depicting weights of different fish species')
Fig2 = px.scatter(df, x= 'Species', y = 'Length', title = 'Bar plot depicting lengths of different fish species')

st.plotly_chart(Fig1)
st.scatter_chart(Fig2)

st.markdown("### Detailed Data View")
st.dataframe(df)
