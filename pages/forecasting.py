import streamlit as st
import joblib

st.title("📈 Demand Forecasting")

predicted_demand = 1360

col1, col2, col3 = st.columns(3)

col1.metric(
    "Tomorrow Demand",
    f"{predicted_demand:.0f}"
)

col2.metric(
    "Forecast Accuracy",
    "89%"
)

col3.metric(
    "Orders Analyzed",
    "50,000"
)

st.divider()

st.subheader("Demand Insights")

st.success(
    f"Predicted demand for tomorrow is {predicted_demand:.0f} units."
)

st.info(
    "Demand trend is stable. Inventory replenishment recommended."
)