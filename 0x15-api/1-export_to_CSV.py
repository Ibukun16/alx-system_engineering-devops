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
    USER_ID = argv[1]
    baseURL = 'https://jsonplaceholder.typicode.com/users'
    empURL = baseURL + '/' + USER_ID
    todoURL = empURL + '/todos'

    responsename = sessionquest.get(empURL)
    USERNAME = responsename.json()['name']

    responsetodo = sessionquest.get(todoURL)
    tasks = responsetodo.json()

    completeTasks = 0
    done = []

    for task in tasks:
        if task['completed']:
            done.append(task)
            completeTasks += 1

    employeeCSV = USER_ID + '.csv'

    with open(employeeCSV, "w", newline='') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for t in tasks:
            TASK_COMPLETED_STATUS = t.get('completed')
            TASK_TITLE = t.get('title')
            writer.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS,
                            TASK_TITLE])
