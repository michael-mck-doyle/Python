'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

base = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")

# convert response to json object
message_back = response.json()
data_body = message_back['data']
#pprint(data_body)


for v in data_body:
    for e in v:
        if e == 'email':
            print(v[e])
