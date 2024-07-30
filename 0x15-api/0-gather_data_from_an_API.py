#!/usr/bin/python3
"""A script that uses a given REST API for an employee ID
and returns information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    empID = argv[1]
    baseURL = 'https://jsonplaceholder.typicode.com/users'
    empURL = baseURL + '/' + empID
    todoURL = empURL + '/todos'

    responsename = requests.get(empURL)
    empNAME = responsename.json().get('name')

    responsetodo = requests.get(todoURL)
    tasks = responsetodo.json()

    completeTasks = 0
    done = []

    for task in tasks:
        if task.get('completed'):
            done.append(task)
            completeTasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empNAME, completeTasks, len(tasks)))

    for task in done:
        print("\t {}".format(task.get('title')))
