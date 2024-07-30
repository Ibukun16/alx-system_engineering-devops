#!/usr/bin/python3
"""A script that uses a given REST API for an employee ID
and returns information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    session_quest = requests.Session()

    empID = argv[1]
    empURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(empID)
    todoURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(empID)

    responsename = session_quest.get(empURL)
    empNAME = responsename.json()['name']

    responsetodo = session_quest.get(todoURL)
    tasks = responsetodo.json()

    completeTasks = 0

    for task in tasks:
        if task['completed']:
            completeTasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empNAME, completeTasks, len(tasks)))

    for task in tasks:
        if task['completed']:
            print("\t " + task.get('title'))
