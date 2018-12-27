
import pymongo
from pymongo import MongoClient
client = MongoClient("localhost", 27017)

db = client.test
collection = db.ncs
docs = collection.find()

for i in docs:
        print(i)
print("============================")

