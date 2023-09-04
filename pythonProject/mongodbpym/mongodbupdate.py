import pymongo
from pymongo import MongoClient

client=MongoClient('localhost',27017)
database=client['mydb']
collection=database['product']
filter={"name":"Iphone"}
result=collection.update_many(filter,{"$set": {"price":"2500"}})
print(result.modified_count)
cursor=collection.find({"name":"Iphone"})
for each in cursor:
    print(each)