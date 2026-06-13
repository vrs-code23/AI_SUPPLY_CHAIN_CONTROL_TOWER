import pandas as pd
import numpy as np

np.random.seed(42)

# ----------------------
# ORDERS
# ----------------------

cities = ["Delhi","Mumbai","Bangalore","Chandigarh","Pune"]

products = [
    "Milk",
    "Bread",
    "Rice",
    "Vegetables",
    "Eggs"
]

orders = []

for i in range(50000):

    qty = np.random.randint(1,20)

    revenue = qty * np.random.randint(50,150)

    orders.append([
        i+1,
        pd.Timestamp("2025-01-01")
        + pd.Timedelta(days=np.random.randint(0,365)),
        np.random.choice(cities),
        np.random.choice(["North","South","East","West"]),
        np.random.choice(products),
        qty,
        revenue
    ])

orders_df = pd.DataFrame(
    orders,
    columns=[
        "order_id",
        "order_date",
        "city",
        "zone",
        "product",
        "quantity",
        "revenue"
    ]
)

orders_df.to_csv("orders.csv",index=False)

# ----------------------
# INVENTORY
# ----------------------

inventory = []

for i in range(100):

    inventory.append([
        i+1,
        np.random.choice([
            "Warehouse_A",
            "Warehouse_B",
            "Warehouse_C"
        ]),
        np.random.choice(products),
        np.random.randint(100,2000),
        np.random.randint(50,300)
    ])

inventory_df = pd.DataFrame(
    inventory,
    columns=[
        "inventory_id",
        "warehouse",
        "product",
        "stock",
        "reorder_level"
    ]
)

inventory_df.to_csv(
    "inventory.csv",
    index=False
)

# ----------------------
# SUPPLIERS
# ----------------------

suppliers = []

for i in range(20):

    suppliers.append([
        i+1,
        f"Supplier_{i+1}",
        np.random.randint(2,15),
        round(np.random.uniform(70,100),2),
        round(np.random.uniform(75,100),2),
        round(np.random.uniform(60,100),2)
    ])

suppliers_df = pd.DataFrame(
    suppliers,
    columns=[
        "supplier_id",
        "supplier_name",
        "lead_time_days",
        "quality_score",
        "on_time_rate",
        "cost_score"
    ]
)

suppliers_df.to_csv(
    "suppliers.csv",
    index=False
)

# ----------------------
# DELIVERIES
# ----------------------

deliveries = []

for i in range(20000):

    distance = np.random.randint(1,25)

    traffic = np.random.randint(1,10)

    rain = np.random.randint(0,2)

    riders = np.random.randint(5,50)

    delay = 1 if (
        traffic > 7
        or rain == 1
    ) else 0

    deliveries.append([
        i+1,
        distance,
        traffic,
        rain,
        riders,
        delay
    ])

deliveries_df = pd.DataFrame(
    deliveries,
    columns=[
        "delivery_id",
        "distance_km",
        "traffic_index",
        "rainfall",
        "rider_count",
        "delayed"
    ]
)

deliveries_df.to_csv(
    "deliveries.csv",
    index=False
)

# ----------------------
# COMPLAINTS
# ----------------------

categories = [
    "Late Delivery",
    "Damaged Product",
    "Missing Item",
    "Wrong Item"
]

severity_levels = [
    "Low",
    "Medium",
    "High"
]

complaints = []

for i in range(5000):

    complaints.append([
        i+1,
        np.random.choice(categories),
        np.random.choice(cities),
        np.random.choice(severity_levels)
    ])

complaints_df = pd.DataFrame(
    complaints,
    columns=[
        "complaint_id",
        "category",
        "city",
        "severity"
    ]
)

complaints_df.to_csv(
    "complaints.csv",
    index=False
)

print("All datasets generated successfully!")