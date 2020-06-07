
# sending body of post message as json file, don't forget to check the "Content-Type" is "application/json" in the headers section

import requests

url = "http://petstore.swagger.io/v2/pet"

#payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"mypet_post_2\"; filename=\"mypet_post_2_send_file_as_body.json\"\r\nContent-Type: application/json\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/json",
    'Accept': "application/json",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Cache-Control': "no-cache",
    'Postman-Token': "8753b7c7-a668-441d-8cf8-4936ab88c5d1,2fa3665c-bfa9-40a0-86f4-2dcbbc4db922",
    'Host': "petstore.swagger.io",
    'accept-encoding': "gzip, deflate",
    'content-length': "219",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }


contents = open('mypet_post_2_send_file_as_body.json', 'rb').read()
response = requests.post(url, data=contents, headers=headers)
print(response.text)

#pprint(response.content)

'''
import requests

url = 'https://api.example.com/api/dir/v1/accounts/9999999/orders'
headers = {'Authorization' : ‘(some auth code)’, 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
r = requests.post(url, data=open('example.json', 'rb'), headers=headers)
'''
'''
# How to translate the curl request below into python?

how to add body from file?

curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d @Post_mypet_1.json
"http://petstore.swagger.io/v2/pet" -o mypet_response_1
'''
