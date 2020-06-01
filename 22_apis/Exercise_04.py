'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
from pprint import pprint


base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 142,
    "first_name": "Jemima",
    "last_name": "Bond",
    "email": "JB@email.com"
}

# here we execute the PUT request
response = requests.put(base_url, json=body)
print(f"Response Code: {response.status_code}")

# GET request to retrieve the new data from the server
key_value_params = {
    "email": "JB@email.com"  # returns user based on email address

}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=key_value_params)
pprint(response.status_code)
pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")
