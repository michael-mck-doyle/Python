import requests
from pprint import pprint


params = {

# enter params here:
    # format: "param": "param value"
}

response = requests.get("http://localhost:8085/student/101", params=params)
pprint(response.status_code)
pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")
