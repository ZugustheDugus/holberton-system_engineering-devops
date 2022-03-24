#!/usr/bin/python3
"""
Export to CSV
"""

import requests
import csv
from sys import argv


def CSV():
    id = argv[1]
    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(id)).json()

    todos = requests.get("https://jsonlaceholder.typicode.com/todos?userId={}".format(id)).json()

    with open("{}.csv".format(id), "w", newline="") as csvFile:
        wrot = csv.writer(csvFile, quotes=csv.QUOTE_ALL)
    for task in todos:
        wrot.writerow([int(id), usr.get("username"),
                        task.get("completed"), task.get("title")])

if __name__ == '__main__':
    CSV()