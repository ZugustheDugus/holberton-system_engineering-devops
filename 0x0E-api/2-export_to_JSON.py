#!/usr/bin/python3
"""
Export Data in JSON based on task 0
"""


def Jason():
    import csv
    import json
    import requests
    from sys import argv
    id = argv[1]
    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id)).json()

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id)).json()

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

    jsonTask = []
    for task in todos:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = usr.get("username")
        jsonTask.append(task_dict)
    json_dict = {}
    json_dict[id] = jsonTask
    with open("{}.json".format(id), "w") as file:
        json.dump(json_dict, file)


if __name__ == '__main__':
    Jason()