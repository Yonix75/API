from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
mongo_uri= os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["onepiece"]

fruits_collection = db["fruits"]
crews_collection = db["crews"]