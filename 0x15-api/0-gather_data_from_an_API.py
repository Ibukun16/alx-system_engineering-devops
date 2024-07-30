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
    baseURL = 'https://jsonplaceholder.typicode.com/users'
    empURL = baseURL + '/' + empID
    todoURL = baseURL + '/' + empID + '/todos'

    responsename = session_quest.get(empURL)
    empNAME = responsename.json()['name']

    responsetodo = session_quest.get(todoURL)
    tasks = responsetodo.json()

    completeTasks = 0
    done_tasks = []

    for task in tasks:
        if task['completed']:
            done_tasks.append(task)
            completeTasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empNAME, completeTasks, len(tasks)))

    for task in done_tasks:
        print("\t " + task.get('title'))
