#!/usr/bin/python3
"""A script that uses a given REST API for an employee ID
and returns information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    sessionquest = requests.Session()
    empID = argv[1]
    baseURL = 'https://jsonplaceholder.typicode.com/users'
    empURL = baseURL + '/' + empID
    todoURL = empURL + '/todos'

    responsename = sessionquest.get(empURL)
    empNAME = responsename.json()['name']

    responsetodo = sessionquest.get(todoURL)
    tasks = responsetodo.json()

    complete = 0
    total_tasks = 0
    done = []

    for task in tasks:
        if task['completed'] is True:
            done.append(task)
            complete += 1

    print("Employee {} is done with tasks({}/{}):"
          format(empNAME, donetasks, totaltasks))

    for task in done:
        tasktitle = task.get('title')
        print("\t {}".format(tasktitle))
