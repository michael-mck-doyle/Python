import requests
from pprint import pprint
import json
'''
response = requests.get("http://api.walmartlabs.com/v1/search?query=ipod&format=json&apiKey=vd3vpvdy423u4h9a9haqjzu9")
#print(response.status_code)
#pprint(f"Header: {response.headers}")
#pprint(f"Body: {response.content}")
pprint(response.status_code)
data = response.json()
pprint(data)

#pprint(f"Header: {response.headers}")
#pprint(f"Body: {response.content}")
'''

params = {
    "query": "ipod",
    "format": "json",
    "apiKey": "vd3vpvdy423u4h9a9haqjzu9"

}

response = requests.get("http://api.walmartlabs.com/v1/search", params=params)
pprint(response.status_code)

print()
pprint(f"Header: {response.headers}")
print()
pprint(f"Body: {response.content}")
