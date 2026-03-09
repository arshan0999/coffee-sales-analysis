import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/coffee_sales.csv")

df['revenue'] = df['transaction_qty'] * df['unit_price']
df['transaction_time'] = pd.to_datetime(df['transaction_time'])
df['hour'] = df['transaction_time'].dt.hour
df['day_of_week'] = df['transaction_time'].dt.day_name()

st.title("Coffee Sales Dashboard")

store = st.selectbox("Select Store Location", df['store_location'].unique())

filtered_df = df[df['store_location'] == store]

hourly_sales = filtered_df.groupby('hour')['revenue'].sum().reset_index()

fig = px.line(hourly_sales, x='hour', y='revenue', title="Hourly Revenue Trend")

st.plotly_chart(fig)