import requests


base_url = "http://localhost:8085/student/101"


head_message = requests.head(base_url)

print(head_message)
print(head_message.content)
print(head_message.headers)
print(head_message.status_code)

