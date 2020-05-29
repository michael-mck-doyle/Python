'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body

'''

import requests
from pprint import pprint

base = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base)
pprint(response.status_code)
pprint(response.encoding)
pprint(response.content)
#response_data = response.json()
#pprint(response.json())
