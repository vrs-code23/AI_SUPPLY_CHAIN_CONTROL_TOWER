import pandas as pd
import mysql.connector

# Database Connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsha@12345",
    database="supply_chain_control_tower"
)


query = """
SELECT product,
AVG(stock) as stock,
AVG(reorder_level) as reorder_level
FROM inventory
GROUP BY product
"""

inventory = pd.read_sql(query, conn)
print("CSV Data loaded directly:", inventory.shape)
# print("forecast data loaded directly:", .shape)

predicted_demand = 1360

inventory["safety_stock"] = 100

inventory["recommended_reorder"] = (
    predicted_demand/5
    + inventory["safety_stock"]
    - inventory["stock"]
)

inventory["recommended_reorder"] = (
    inventory["recommended_reorder"]
    .apply(lambda x: max(0, round(x)))
)

print(inventory[
    [
        "product",
        "stock",
        "recommended_reorder"
    ]
])