'''
Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

** Try building a Python GUI to submit the requests
- add buttons for each Method type e.g.
It is your responsibility to build out the application to handle all menu options above.

Consider using:
- ** Try building a Python GUI to submit the requests
- try using web page / html to submit and return the requests
'''

import requests
from pprint import pprint
import tkinter
from tkinter import ttk
print()
print("Action Menu:")
print ("""
    1. Create a new account
    2. View all your tasks
    3. View your completed tasks
    4. View only your incomplete tasks
    5. Create a new task
    6. Update an existing task
    7. Delete a task
    """)

action = int(input("Please enter an action from the menu: "))
base = "http://demo.codingnomads.co:8080/tasks_api/users"

#
#body = {
#       "first_name": "Wayne's",  # add first name inside quotes
#        "last_name": "World",  # add last name inside quotes
#        "email": "waynesworld@email.com"  # add email inside quotes
#    }
#

if action == 1:
    print()
    print("please enter details to create an account: ")
    first_name = input("enter first name: ")
    surname = input("enter surname: ")
    email = input("enter email: ")
    body = {
        "first_name": first_name,  # add first name inside quotes
        "last_name": surname,  # add last name inside quotes
        "email": email  # add email inside quotes
    }
    response = requests.post(base, json=body)
    pprint(response.status_code)
    pprint(response.encoding)
    pprint(response.content)
    with open('POST_response_1.txt', 'w') as f_out:
        f_out.write(str(response.text))

elif action == 2:
    response = requests.get(base)
    pprint(response.status_code)
    pprint(response.encoding)
    pprint(response.content)
    with open('GET_response.txt_1.txt', 'w') as f_out:
        f_out.write(str(response.text))



