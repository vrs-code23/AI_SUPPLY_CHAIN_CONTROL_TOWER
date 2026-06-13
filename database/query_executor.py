# import mysql.connector
# import pandas as pd

import mysql.connector

print("Trying to connect...")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsha@12345",
    database="supply_chain_control_tower"
)

print("Connected Successfully")
# def run_query(sql_query):

#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="varsha@12345",
#         database="supply_chain_control_tower"
#     )

#     result = pd.read_sql(sql_query, conn)

#     conn.close()

#     return result