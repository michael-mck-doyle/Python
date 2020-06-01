'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests
from pprint import pprint


base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.delete(base_url + "/141")
print(response.status_code)


params = {
    "id": "142"
}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=params)
pprint(response.status_code)
pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")