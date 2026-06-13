import pandas as pd
import mysql.connector
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Database Connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsha@12345",
    database="supply_chain_control_tower"
)

# query = """
# SELECT *
# FROM deliveries
# """
query = "SELECT * FROM deliveries"

df = pd.read_sql(query, conn)

conn.close()

# Features

X = df[
    [
        "distance_km",
        "traffic_index",
        "rainfall",
        "rider_count"
    ]
]

# Target
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

y = df["delayed_status"]

# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"\nAccuracy: {accuracy:.2f}")

# Save Model

joblib.dump(
    model,
    "delay_model.pkl"
)

print("Delay Model Saved!")

sample = [[
    12,   # distance
    8,    # traffic
    1,    # rainfall
    10    # riders
]]

prediction = model.predict(sample)

print("\nPrediction:")

if prediction[0] == 1:
    print("Delivery likely delayed")
else:
    print("Delivery likely on time")