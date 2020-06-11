import requests

url = "http://localhost:8085/student/1ist"

payload = ""
headers = {

    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
