import pymongo
from pymongo import MongoClient

client=MongoClient('localhost',27017)
database=client['mydb']
print("DB is created")
collection=database['product']
print("collection is created")
products=[{
    "name":"Mac",
    "price":"1300"
},
{
    "name":"Dell",
    "price":"1300"
}

]
result=collection.insert_many(products)
print(result.inserted_ids)
