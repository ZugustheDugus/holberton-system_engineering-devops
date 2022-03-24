#!/usr/bin/python3
"""
Gather Data from an API
"""

import sys
import requests

if __name__ == "__main__":

    try:
        usr_id = sys.argv[1]
        id = int(usr_id)

    except:
        print("ID not INT")

    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                    .format(id))
    name = usr.json()["name"]

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    todo_all = 0
    todo_cmplt = 0

    for j in todos.json():
        if j['usr_id'] == id:
            todo_all += 1
        if j['usr_id'] == id:
            todo_cmplt += 1

print("Employee {} is done with tasks({}/{}):".format(name, todo_cmplt, todo_all))
for j in todos.json():
    if j["usr_id"]:
        print("\t {}".format(j['title']))
