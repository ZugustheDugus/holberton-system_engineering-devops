#!/usr/bin/python3
"""
Gather Data from an API
"""
import json
from sys import argv
from urllib import request

if __name__ == "__main__":

    rqst = request.urlopen('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))

    usr = json.loads(rqst.read())

    rqst = request.urlopen('https://jsonplaceholder.typicode.com/todos')
    todo_all = json.loads(rqst.read())

    rqst.close()

    todo = []
    success = 0

    for item in all:
        if str(item.get("user.id")) == argv[1]:
            todo.append(item)
            if item.get("completed") is True:
                success += 1

    print("Employee {} is done with tasks({}/{}):".
            format(usr.get("name"), success, len(todo)))

    for item in todo:
        if item.get("completed") is True:
            print("\t {}".format(item.get("title")))