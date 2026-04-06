import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb+srv://klin43_db_user:3cxfsJDDSl7XRwjc@cluster0.wymkhmw.mongodb.net/?appName=Cluster0")

db = client["ev_db"]
collection = db["vehicles"]
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
data = df.to_dict(orient="records")

for i in range(0, len(data), 1000):
    collection.insert_many(data[i:i+1000])
