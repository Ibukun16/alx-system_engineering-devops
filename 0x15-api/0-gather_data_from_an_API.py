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
    EMPLOYEE_NAME = responsename.json()['name']

    responsetodo = sessionquest.get(todoURL)
    tasks = responsetodo.json()

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    done = []

    for task in tasks:
        if task['completed']:
            done.append(task)
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in done:
        TASK_TITLE = task.get('title')
        print("\t {}".format(TASK_TITLE))
