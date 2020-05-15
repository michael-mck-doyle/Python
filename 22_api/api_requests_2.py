import requests
from pprint import pprint
import json

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

print(f"Response Content: {response.content}")
print(f"Response Status Code: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Response Encoding: {response.encoding}")
print(f"Response URL: {response.url}")