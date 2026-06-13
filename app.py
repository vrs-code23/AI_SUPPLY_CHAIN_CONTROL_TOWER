import streamlit as st

st.set_page_config(
    page_title="AI Supply Chain Control Tower",
    layout="wide"
)

st.title("🚚 AI Supply Chain Control Tower")

st.markdown("### Real-Time Supply Chain Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Orders", "50,000")
col2.metric("Deliveries", "20,000")
col3.metric("Suppliers", "20")
col4.metric("Forecast", "1360")

st.divider()

st.success("Demand Forecasting")
st.success("Inventory Optimization")
st.success("Supplier Risk Analytics")
st.success("Logistics Delay Prediction")

st.info(
    "Navigate through the sidebar to access individual analytics modules."
)