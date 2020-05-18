import requests
from pprint import pprint
import json

response = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=meyekkul")
print(response.status_code)
print()
pprint(f"Header: {response.headers}")
print()
pprint(f"Body: {response.content}")

