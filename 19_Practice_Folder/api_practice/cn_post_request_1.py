import requests
from pprint import pprint
import json
'''
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "[NICK-NACK]",#add first name inside quotes
    "last_name": "[PADDYWACK]",#add last name inside quotes
    "email": "[givethedogabone@email.com]"#add email inside quotes
}

post_data = requests.post(base_url, json=body)
x = post_data.content
print(x)
# print the status code (hopefully it's 200 which means all is well)
print(f"Response Code: {post_data.status_code}")
print(post_data.json())

# let's make a GET request to retrieve the new data from the server
#response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
# print the data - see your new record?
#pprint(f"Response Content: {response.content}")
'''

base_url = "https://virtserver.swaggerhub.com/SporranSolution/Tasks/1.0.0/inventory"

body = {
  "name": "Phone Adapter",
  "description": "adding adapter"
}

post_data = requests.post(base_url, json=body)
x = post_data.content
print(f"Response Code: {post_data.status_code}")
pprint(post_data.content)
pprint(post_data.text)
pprint(post_data.request)






