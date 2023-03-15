
from email import header
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


######################## Read ##############################


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# get_data()

######################## Create ##############################


def post_data():
    data = {
        'name': "Saj",
        'roll': 128,
        'city': 'pabna',
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


post_data()


######################## Update ##############################
def update_data():
    data = {
        'id': 21,
        'name': 'Akmal',
        'roll': 112,
        'city': 'Natore',
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


# update_data()


######################## Delete ##############################

def delete_data():
    data = {'id': 19}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


# delete_data()
