import os
import streamlit as st
import google.generativeai as genai
from database.query_executor import run_query

genai.configure(api_key=os.environ.get("GCP_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 Supply Chain AI Copilot")

question = st.text_input("Ask a Supply Chain Question")

if question:

    prompt = f"""
    You are a MySQL expert.

    Database Tables:

    orders(
        order_id,
        order_date,
        city,
        zone,
        product,
        quantity,
        revenue
    )

    inventory(
        inventory_id,
        warehouse,
        product,
        stock,
        reorder_level,
        safety_stock,
        recommended_reorder
    )

    suppliers(
        supplier_id,
        supplier_name,
        lead_time_days,
        quality_score,
        on_time_rate,
        cost_score
    )

    deliveries(
        delivery_id,
        distance_km,
        traffic_index,
        weather_score,
        delayed
    )

    Convert the user's question into ONLY a SQL query.

    User Question:
    {question}
    """

    response = model.generate_content(prompt)
    sql_query = response.text

    sql_query = sql_query.replace("```sql","").replace("```","")

    st.subheader("Generated SQL")
    st.code(sql_query)

    try:

        result = run_query(sql_query)

        st.subheader("Results")
        st.dataframe(result)

    except Exception as e:

        st.error(f"SQL Error: {e}")
        
# sql_query = sql_query.strip()

# if not sql_query.lower().startswith("select"):
#     st.error("Only SELECT queries allowed")
#     st.stop()