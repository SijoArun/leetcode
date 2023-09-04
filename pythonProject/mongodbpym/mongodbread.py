import pymongo
from pymongo import MongoClient

client=MongoClient('localhost',27017)
database=client['mydb']
collection=database['product']
result=collection.find_one()
print(result)
cursor=collection.find({"name":"Mac"})
for each in cursor:
    print(each)