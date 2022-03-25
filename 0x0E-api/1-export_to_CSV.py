#!/usr/bin/python3
"""
Export to CSV based on task 0
"""


import requests
import csv
from sys import argv


def CSV():
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

    with open("{}.csv".format(id), "w", newline="") as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([int(id), usr.get("username"),
                            task.get("completed"), task.get("title")])


if __name__ == '__main__':
    CSV()
