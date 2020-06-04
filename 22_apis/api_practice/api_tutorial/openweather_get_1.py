import requests
from pprint import pprint


key_value_params = {
    "zip": "Ca$HMonEY@gmail.com", #returns user based on email address
    "units": "imperial",
    "appid": "b67bc3439ff0f7f7ff6d0abc779d0bd8"

}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=key_value_params)
pprint(response.status_code)
pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")