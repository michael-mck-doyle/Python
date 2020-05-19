import requests
from pprint import pprint


base_url = "http://localhost:8085/student/"
delete_student = requests.delete("http://localhost:8085/student/" + "/102")
print(delete_student.status_code)
pprint(delete_student.content)
pprint(delete_student.headers)

'''
params = {
    "id": "124"
}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=params)
pprint(response.status_code)
pprint(f"Header: {response.headers}")
pprint(f"Body: {response.content}")
'''
