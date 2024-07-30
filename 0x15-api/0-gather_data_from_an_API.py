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
    empNAME = responsename.json()['username']

    responsetodo = sessionquest.get(todoURL)
    tasks = responsetodo.json()

    number_of_done_tasks = 0
    total_number_of_tasks = len(tasks)
    done = []

    for task in tasks:
        if task['completed']:
            done.append(task)
            number_of_done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(empNAME, number_of_done_tasks, total_number_of_tasks))

    for task in done:
        task_title = task.get('title')
        print("\t {}".format(task_title))
