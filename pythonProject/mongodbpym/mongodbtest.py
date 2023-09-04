import pymongo
from pymongo import MongoClient

client=MongoClient('localhost',27017)
database=client['mydb']
print("DB is created")
collection=database['product']
print("collection is created")
product1={
    "name":"Samsung",
    "price":"1300"
}
result=collection.insert_one(product1)
print(result.inserted_id)
