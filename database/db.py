import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsha@12345",
    database="supply_chain_control_tower"
)

cursor = conn.cursor()

print("Database Connected Successfully!")