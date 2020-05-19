import requests
from pprint import pprint
base_url = "http://localhost:8085/student/"

body = {
    "firstName": "Money",
    "lastName": "Bags",
    "email": "money.bagsn@massaQuisqueporttitor.org",
    "programme": "Financial Analysis",
    "courses": [
        "Accounting",
        "Statistics",
        "Investing"
    ]
}

post_data = requests.post(base_url, json=body)
x = post_data.content
print(x)
pprint(post_data.status_code)
pprint(f"Header: {post_data.headers}")
pprint(f"Body: {post_data.content}")

