#!/usr/bin/python3
"""
Gather Data from an API (this is task 0)
"""

import requests
from sys import argv


def todo():

    id = argv[1]
    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id)).json()

    to_do = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(id)).json()

    complete = []

    for task in to_do:
        if task.get("completed") is True:
            complete.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(usr.get('name'), len(complete), len(to_do)))
    for task in complete:
        print("\t {}".format(task))


if __name__ == '__main__':
    todo()
