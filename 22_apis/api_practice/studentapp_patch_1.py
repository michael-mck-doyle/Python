
import requests
from pprint import pprint


base_url = "http://localhost:8085/student/101"

body = {
    "email": "FEELING.LUCKY@LUCKYME.com" #add email inside quotes
}

post_data = requests.patch(base_url, json=body)

print(f"Response Code: {post_data.status_code}")
print(post_data.json())




