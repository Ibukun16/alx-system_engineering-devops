#!/usr/bin/python3
"""A script that build on the previous task which uses REST API
to obtain information about an employee TODO list then export the
data in the CSV format.
"""

import csv
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

    completeTasks = 0
    done = []

    for task in tasks:
        if task['completed']:
            done.append(task)
            completeTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(empNAME, completeTasks, len(tasks)))

    for task in done:
        print("\t {}".format(task.get('title')))
