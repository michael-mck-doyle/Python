import requests
from pprint import pprint

url = "http://petstore.swagger.io/v2/pet/12000"

headers = {
    'Accept': "application/json",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Cache-Control': "no-cache",
    'Postman-Token': "6591a2fa-0332-4749-a74d-e75b51814ebf,eca1d633-91e3-4df5-90ff-3c4021d7776d",
    'Host': "petstore.swagger.io",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

pprint(response.text)
