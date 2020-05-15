import requests
from pprint import pprint

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?email=caden@email.com")
print(response.status_code)
pprint(response.json)

#is the same as

params = {
    "email": "ryan@codingnomads.co"
}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=params)
print(response.status_code)
pprint(response.json())


'''
base_url = "http://demo.codingnomads.co:8080/tasks_api/tasks?userId=1&complete=true"
response = requests.get(base_url)
print(response.status_code)
pprint(response.raw)

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?email=ryan@codingnomads.co")
#print(response.status_code)
pprint(response.json())
'''