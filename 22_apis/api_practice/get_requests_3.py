import requests
from pprint import pprint
import json

base_url = "http://demo.codingnomads.co:8080/tasks_api/users?"
response = requests.get(base_url)

message_back = response.json()
#x = message_back['data'][2]['email']
#print(f"the email address returned is {x}")


#for x, y in message_back.items():
  #print(x, y)

#[{'id': 52, 'first_name': 'JMONEY BAG$$$$', 'last_name': 'mONeY, MoNeY, MONEY', 'email': 'Ca$HMonEY@gmail.com', 'createdAt': 1569290181000, 'updatedAt': 1569349264000}]
