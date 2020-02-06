from kvs import KVS
from redis import Redis
from pymemcache.client import Client as Memcached
import plyvel, shelve, pickle, msgpack
import json

file=open("artist.json")
db = plyvel.DB('testdb', create_if_missing=True)

num=0
for f in file:
    object=json.loads(f)
    db.put(b'name',object["name"])
    if num==0:

      kvs = KVS(object)
      # print(list(kvs.items()))
      break
print(db.get("name"))