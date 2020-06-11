import requests
from pprint import pprint

'''
base_url = "http://localhost:8085/student/101"

options_available = requests.options(base_url)  # shows the actions that are available on a particular url e.g. what methods, GET, POST, PUT etc
                                                # and gets informtion on API's

print(options_available.status_code)
print(options_available)
print(options_available.content)
print(options_available.headers)
'''

'''
The response from the options request above shows that PUT,DELETE,PATCH,GET,HEAD methods can be used on url http://localhost:8085/student/101
{'Allow': 'PUT,DELETE,PATCH,GET,HEAD', 'Content-Length': '0', 'Date': 'Tue, 19 May 2020 08:18:19 GMT'}

'''
base_url = "https://pokeapi.co/docs/v2.html#pokemon"

options_available = requests.options(base_url)

pprint(options_available.status_code)
pprint(options_available)
pprint(options_available.content)
pprint(options_available.headers)
