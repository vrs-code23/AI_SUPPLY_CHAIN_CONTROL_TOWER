import streamlit as st
import pandas as pd
import mysql.connector

st.title("🏭 Supplier Risk Analytics")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsha@12345",
    database="supply_chain_control_tower"
)

suppliers = pd.read_sql(
    "SELECT * FROM suppliers",
    conn
)

conn.close()

# Risk Score

suppliers["risk_score"] = (
    (100 - suppliers["quality_score"]) * 0.35
    +
    (100 - suppliers["on_time_rate"]) * 0.35
    +
    suppliers["lead_time"] * 2
    +
    (100 - suppliers["cost_score"]) * 0.10
)

# Risk Level

def classify(score):
    if score < 20:
        return "LOW"
    elif score < 35:
        return "MEDIUM"
    else:
        return "HIGH"

suppliers["risk_level"] = suppliers["risk_score"].apply(classify)

# Supplier Score

suppliers["supplier_score"] = (
    suppliers["quality_score"] * 0.4
    +
    suppliers["on_time_rate"] * 0.4
    +
    suppliers["cost_score"] * 0.2
)

suppliers["rank"] = suppliers[
    "supplier_score"
].rank(
    ascending=False,
    method="dense"
)

top5 = suppliers.sort_values(
    by="supplier_score",
    ascending=False
).head(5)

high_risk = suppliers[
    suppliers["risk_level"] == "HIGH"
]

col1, col2, col3 = st.columns(3)

col1.metric("Suppliers", len(suppliers))
col2.metric("Top Suppliers", len(top5))
col3.metric("High Risk", len(high_risk))

st.subheader("🏆 Top 5 Suppliers")
st.dataframe(top5)

st.subheader("⚠ High Risk Suppliers")
st.dataframe(high_risk)

st.subheader("📋 All Suppliers")
st.dataframe(suppliers)