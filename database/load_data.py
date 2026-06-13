import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsha@12345",
    database="supply_chain_control_tower"
)

cursor = conn.cursor()

# -------------------
# INVENTORY
# -------------------

inventory = pd.read_csv("data/inventory.csv")

for _, row in inventory.iterrows():

    cursor.execute("""
    INSERT IGNORE INTO inventory
    VALUES (%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

print("Inventory Loaded!")

# -------------------
# SUPPLIERS
# -------------------

suppliers = pd.read_csv("data/suppliers.csv")

for _, row in suppliers.iterrows():

    cursor.execute("""
    INSERT IGNORE INTO suppliers
    VALUES (%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

print("Suppliers Loaded!")

# -------------------
# DELIVERIES
# -------------------

deliveries = pd.read_csv("data/deliveries.csv")

for _, row in deliveries.iterrows():

    cursor.execute("""
    INSERT IGNORE INTO deliveries
    VALUES (%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

print("Deliveries Loaded!")

# -------------------
# COMPLAINTS
# -------------------

complaints = pd.read_csv("data/complaints.csv")

for _, row in complaints.iterrows():

    cursor.execute("""
    INSERT IGNORE INTO complaints
    VALUES (%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

print("Complaints Loaded!")

conn.close()

print("All Data Loaded Successfully!")