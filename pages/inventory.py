import streamlit as st
import pandas as pd

st.title("📦 Inventory Optimization")

inventory = pd.read_csv("data/inventory.csv")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Products",
    len(inventory)
)

col2.metric(
    "Safety Stock",
    "100"
)

col3.metric(
    "Reorder Alerts",
    (inventory["current_stock"] < 100).sum()
)

st.divider()

st.subheader("Inventory Data")

st.dataframe(inventory)

st.subheader("Low Stock Products")

low_stock = inventory[
    inventory["current_stock"] < 100
]

st.dataframe(low_stock)