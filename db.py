from pymongo import MongoClient

client = MongoClient("mongodb+srv://contactyonibena_db_user:9Y4eZoy57FqiGPAa@cluster0.ov7ongd.mongodb.net/?appName=Cluster0")
db = client["onepiece"]

fruits_collection = db["fruits"]
crews_collection = db["crews"]