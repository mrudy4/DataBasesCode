
from pymongo import MongoClient
# Replace the uri string with your MongoDB deployment's connection string.
client = MongoClient(
    "mongodb://localhost:27017/?directConnection=true"
)
# database and collection code goes here
db = client.moviesDB
coll = db.moviesCollection
# find code goes here
cursor = coll.find()
# iterate code goes here
for doc in cursor:
    print(doc)
# Close the connection to MongoDB when you're done.
client.close()