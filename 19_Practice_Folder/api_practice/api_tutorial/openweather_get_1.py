import requests
from pprint import pprint


key_value_params = {
    "zip": 90250, #returns user based on email address
    "units": "imperial",
    "appid": "b67bc3439ff0f7f7ff6d0abc779d0bd8"

}

response = requests.get(" https://api.openweathermap.org/data/2.5/weather", params=key_value_params)
pprint(response.status_code)
pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")