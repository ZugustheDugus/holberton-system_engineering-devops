#!/usr/bin/python3
"""
Export data in the JSON format, but it's a dict list of dicts
based on task 0
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
    usr = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    """
    Prints to screen tasks the employee has done and which tasks
    """
    completedTask = []
    for task in todos:
        if task.get("completed") is True:
            completedTask.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(usr.get('name'), len(completedTask), len(todos)))
    for task in completedTask:
        print("\t {}".format(task))

    """
    Exports completed tasks to csv file
    """
    with open("{}.csv".format(id), "w", newline="") as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([int(id), usr.get("username"),
                            task.get("completed"), task.get("title")])
    """Exports all tasks as json files"""
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


def save_all():
    """
    Records all tasks from all employees in JSON format
    """
    usrs = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    dict = {}
    usrnames = {}
    for usr in usrs:
        uid = usr.get("id")
        dict[uid] = []
        usrnames[uid] = usr.get("username")
    for task in todos:
        taskd = {}
        uid = task.get("userId")
        taskd["username"] = usrnames.get(uid)
        taskd["task"] = task.get("title")
        taskd["completed"] = task.get("completed")
        dict.get(uid).append(taskd)

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict, file)


if __name__ == '__main__':
    import json
    import requests
    from sys import argv
    try:
        Jason()
    except Exception:
        save_all()