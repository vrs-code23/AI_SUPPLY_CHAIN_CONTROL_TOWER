import pandas as pd
import mysql.connector

# Database Connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsha@12345",
    database="supply_chain_control_tower"
)

# Read Supplier Data

query = """
SELECT *
FROM suppliers
"""

suppliers = pd.read_sql(query, conn)

# ------------------------
# Supplier Risk Score
# ------------------------

suppliers["risk_score"] = (
    (100 - suppliers["quality_score"]) * 0.35
    +
    (100 - suppliers["on_time_rate"]) * 0.35
    +
    suppliers["lead_time_days"] * 2
    +
    (100 - suppliers["cost_score"]) * 0.10
)

# ------------------------
# Risk Classification
# ------------------------

def classify_risk(score):

    if score < 20:
        return "LOW"

    elif score < 35:
        return "MEDIUM"

    else:
        return "HIGH"

suppliers["risk_level"] = suppliers["risk_score"].apply(classify_risk)
suppliers["supplier_score"] = (
    suppliers["quality_score"] * 0.4
    +
    suppliers["on_time_rate"] * 0.4
    +
    suppliers["cost_score"] * 0.2
)

suppliers["rank"] = (
    suppliers["supplier_score"]
    .rank(
        ascending=False,
        method="dense"
    )
)
# Sort Highest Risk First

suppliers = suppliers.sort_values(
    by="risk_score",
    ascending=False
)

print("\nSupplier Risk Ranking\n")

print(
    suppliers[
        [
            "supplier_name",
            "risk_score",
            "risk_level"
        ]
    ]
)
high_risk = suppliers[
    suppliers["risk_level"] == "HIGH"
]

print("\nHigh Risk Suppliers:\n")

print(
    high_risk[
        [
            "supplier_name",
            "risk_score"
        ]
    ]
)
high_risk = suppliers[
    suppliers["risk_level"] == "HIGH"
]
conn.close()