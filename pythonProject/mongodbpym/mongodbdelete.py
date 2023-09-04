import pymongo
from pymongo import MongoClient

client=MongoClient('localhost',27017)
database=client['mydb']
collection=database['product']
filter={"name":"Mac"}
result=collection.delete_many(filter)
print(result.deleted_count)
cursor=collection.find(filter)
for each in cursor:
    print(each)