#!/usr/bin/python3
"""
Gather Data from an API
"""
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
    .format(id)).json()

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
    .format(id)).json()

    complete = []

    for task in todos:
        if task.get("completed") is True:
            complete.append(task.get("title"))
        print("Employee {} is done with tasks({}/{}):"
            .format(usr.get('name'), len(complete), len(todos)))
        for task in complete:
            print("\t {}".format(task))
