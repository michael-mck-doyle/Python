
import requests
from pprint import pprint
url = "http://petstore.swagger.io/v2/pet"

# querystring = {}   , params=querystring
payload = "@mypet_post_2.json"

headers = {
    "Content-Type: application/json"
    "Accept: application/json"
    }

response = requests.request("POST", url, headers=headers, data=payload)

pprint(response.text)


'''
# How to translate the curl request below into python?

curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d @Post_mypet_1.json
"http://petstore.swagger.io/v2/pet" -o mypet_response_1
'''
