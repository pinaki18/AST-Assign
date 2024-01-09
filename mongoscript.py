import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient()

client = MongoClient("mongodb+srv://test:test123@cluster0.otzsx8i.mongodb.net/")

db = client.indeed

jobs = db.test_collection

doc = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

post_id = jobs.insert_one(doc).inserted_id
