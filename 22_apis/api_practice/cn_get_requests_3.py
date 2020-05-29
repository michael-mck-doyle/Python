import requests
from pprint import pprint
import json

base_url = "http://demo.codingnomads.co:8080/tasks_api/users?"
response = requests.get(base_url)

message_back = response.json()

# return the keys of the json object to identify which one holds the data
message_keys = message_back.keys()
pprint(message_keys)

# accessing individual values of the dictionary
data = message_back['data']
data1 = (data[7])
print(data1)
data2 = data1['last_name']
pprint(data2)

# this is the same approach as above for extracting information, except that it all takes place on one line of code
data3 = message_back['data'][22]['last_name']
print(data3)

#x = message_back['data'][2]['email']
#print(f"the email address returned is {x}")


#for x, y in message_back.items():
  #print(x, y)

#[{'id': 52, 'first_name': 'JMONEY BAG$$$$', 'last_name': 'mONeY, MoNeY, MONEY', 'email': 'Ca$HMonEY@gmail.com', 'createdAt': 1569290181000, 'updatedAt': 1569349264000}]
