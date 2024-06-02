from faker import Faker
import json
from ulid import ULID
import uuid


fake = Faker()

ulid_resource = {
    "data": []
}

uuid_resource = {
    "data": []
}

ulids = []
uuids = []

for itr in range(1, 100000):
    data = {
        "name": fake.name(),
        "description": fake.text(100)
    }

    _ulid = str(ULID().generate())
    _uuid = str(uuid.uuid4())

    data["id"] = _ulid
    ulid_resource["data"].append(data)
    ulids.append(_ulid)

    data["id"] = _uuid
    uuid_resource["data"].append(data)
    uuids.append(_uuid)


with open('uuid_mock_data.json', 'w') as f:
    json.dump(uuid_resource, f)

with open('ulid_mock_data.json', 'w') as f:
    json.dump(ulid_resource, f)

with open('ulids.json', 'w') as f:
    json.dump({"ids": ulids}, f)

with open('uuids.json', 'w') as f:
    json.dump({"ids": uuids}, f)

