import streamlit as st
import pandas as pd
import mysql.connector

st.title("🚚 Logistics Delay Analytics")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsha@12345",
    database="supply_chain_control_tower"
)

deliveries = pd.read_sql(
    "SELECT * FROM deliveries",
    conn
)

conn.close()

total_deliveries = len(deliveries)

delayed_status = deliveries[
    deliveries["delayed_status"] == 1
]

delay_rate = round(
    len(delayed_status) / total_deliveries * 100,
    2
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Deliveries",
    total_deliveries
)

col2.metric(
    "Delayed_status",
    len(delayed_status)
)

col3.metric(
    "Delay Rate",
    f"{delay_rate}%"
)

st.divider()

st.subheader("Delayed Deliveries")

st.dataframe(delayed_status)

st.subheader("Delivery Dataset")

st.dataframe(deliveries)