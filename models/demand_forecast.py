import pandas as pd
import mysql.connector
from sklearn.linear_model import LinearRegression
import joblib

# Database Connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsha@12345",
    database="supply_chain_control_tower"
)

query = """
SELECT order_date, quantity
FROM orders
"""

df = pd.read_sql(query, conn)

# Daily Demand

daily = df.groupby("order_date")["quantity"].sum().reset_index()

daily["day_number"] = range(len(daily))

X = daily[["day_number"]]
y = daily["quantity"]

# Train Model

model = LinearRegression()

model.fit(X, y)

# Predict Tomorrow

next_day = [[len(daily)]]

prediction = model.predict(next_day)

print(
    f"Predicted Demand Tomorrow: {prediction[0]:.2f}"
)

# Save Model

joblib.dump(
    model,
    "demand_model.pkl"
)

print("Model Saved!")