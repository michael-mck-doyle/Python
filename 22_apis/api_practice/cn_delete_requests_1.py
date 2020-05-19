import requests
from pprint import pprint
import json

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.delete(base_url + "/125")
print(response.status_code)


params = {
    "id": "124"
}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=params)
pprint(response.status_code)
pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")

