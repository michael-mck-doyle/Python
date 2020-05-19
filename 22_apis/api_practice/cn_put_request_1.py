import requests
from pprint import pprint
import json
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 135,
    "first_name": "NEW_NAME",
    "last_name": "NEW_NAME",
    "email": "new_name@email.com"
}

# here we execute the PUT request
response = requests.put(base_url, json=body)
# print the status code (hopefully it's 200 which means all is well)
print(f"Response Code: {response.status_code}")

# let's make a GET request to retrieve the new data from the server
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?email:givethedogabone@email.com")
# print the data - see your updated record?
pprint(f"Response Content: {response.content}")
print()
print()
print(response.json())

