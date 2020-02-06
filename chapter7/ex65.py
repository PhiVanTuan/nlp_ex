import pymongo
import json
file=open("artist.json")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.test_database
artist_table=db['artist']

x=artist_table.find( {"tags": {"value":"dance" }}).sort('rating.count', -1)
for i in x:
    print(i)