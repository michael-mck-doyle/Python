'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests
from pprint import pprint
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "[Bond]",#add first name inside quotes
    "last_name": "[James Bond]",#add last name inside quotes
    "email": "[007@email.com]"#add email inside quotes
}

post_data = requests.post(base_url, json=body)
print(f"Response Code: {post_data.status_code}")
print(post_data.json())

# GET request to retrieve the new data from the server
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users/")
pprint(f"Response Content: {response.content}")