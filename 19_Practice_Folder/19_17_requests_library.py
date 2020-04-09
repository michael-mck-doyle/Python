'''

The requests library is the de facto standard for making HTTP requests in Python
Requests - Requests’ is a simple, easy-to-use HTTP library written in Python.

requests is different from urllib - what are the differences

 References
 Python requests - https://realpython.com/python-requests/
 HTTP Request Methods - https://www.w3schools.com/tags/ref_httpmethods.asp


First, it supports a fully restful API, and is as easy as:
import requests

resp = requests.get('http://www.mywebsite.com/user')
resp = requests.post('http://www.mywebsite.com/user')
resp = requests.put('http://www.mywebsite.com/user/put')
resp = requests.delete('http://www.mywebsite.com/user/delete')

Regardless of whether GET / POST, you never have to encode parameters again, it simply takes a dictionary as an argument and is good to go:

userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}
resp = requests.post('http://www.mywebsite.com/user', data=userdata)

Plus it even has a built in JSON decoder (again, I know json.loads() isn't a lot more to write, but this sure is convenient):

resp.json()

Or if your response data is just text, use:

resp.text

This is just the tip of the iceberg. This is the list of features from the requests site:

International Domains and URLs
Keep-Alive & Connection Pooling
Sessions with Cookie Persistence
Browser-style SSL Verification
Basic/Digest Authentication
Elegant Key/Value Cookies
Automatic Decompression
Unicode Response Bodies
Multipart File Uploads
Connection Timeouts
.netrc support
List item
Python 2.6—3.4
Thread-safe


'''

import requests
bbc_txt = requests.get('https://bbc.co.uk').text
print()
print()
print("request returned as text")
print(bbc_txt)

