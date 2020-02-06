import pymongo
import json
file=open("artist.json")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.test_database
artist_table=db['artist']

for f in file:
    str = json.loads(f)
    artist_table.insert_one(str)
    print(f)

print(artist_table)