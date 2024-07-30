#!/usr/bin/python3
"""A script that uses a given REST API for an employee ID
and returns information about his/her TODO list progress,
then export the data in the json format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    fname = "todo_all_employees.json"
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    userid = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    with open(fname, mode='w') as filename:
        d = {i.get("id"): [{"username": i.get("username"),
                           "task": task.get("title"),
                            "completed": task.get("completed")} for task
                           in todos
                           if i.get('id') == task.get('userId')]
             for i in userid}
        json.dump(d, filename)
