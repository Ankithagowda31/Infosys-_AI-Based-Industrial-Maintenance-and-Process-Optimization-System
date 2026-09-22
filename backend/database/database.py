from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["predictive_maintenance"]

prediction_collection = db["predictions"]
