from pymongo.mongo_client import MongoClient
import uuid
from datetime import datetime
import json

# Mongo Db Connection
MONGO_CONN_STR = "mongodb://localhost:27017"
mongo_client = MongoClient(MONGO_CONN_STR)
database = mongo_client['ulid_vs_uuid']
collection = database["uuid_no_index"]

mock_data = json.load(open('uuid_mock_data.json', 'r'))["data"]

start_time = datetime.now()

for data in mock_data:
    collection.insert_one(data)

end_time = datetime.now()
difference = end_time - start_time
print(f"UUID time {difference}")

