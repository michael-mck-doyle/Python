import requests
from pprint import pprint
import json

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?email=Ca$HMonEY@gmail.com")
#print(response.status_code)
#pprint(f"Header: {response.headers}")
#pprint(f"Body: {response.content}")
data = response.json()
print(data)

print()
print("...is the same as")
print()

params = {
    "email": "Ca$HMonEY@gmail.com"
}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=params)
pprint(response.status_code)
pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")



#print(f"Response Content: {response.content}")
#pprint(response.json)
#pprint(response.content)
#pprint(f"Response Content: {response.content}")
#print(response.content)



# Response Content: b'{"data":[{"id":3,"first_name":"Caden5","last_name":"MacKenzie5","email":"caden@email.com","createdAt":1549560964000,"updatedAt":1585933084000}

