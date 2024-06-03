from fastapi import FastAPI, HTTPException
from pymongo.mongo_client import MongoClient

app = FastAPI()

# Mongo Db Connection
MONGO_CONN_STR = "mongodb://localhost:27017"
mongo_client = MongoClient(MONGO_CONN_STR)
database = mongo_client['ulid_vs_uuid']
collection = database["ulid_no_index"]

@app.get("/ids/{id_val}")
def read_item(id_val: str):
    res = collection.find_one({"id": id_val}, {'_id':0})
    if res['id'] == id_val:
        return {"status": "success"}
    else:
        return {"status": "failure"}