#!/usr/bin/python3
"""A script that uses a given REST API for an employee ID
and returns information about his/her TODO list progress,
then export the data in JSON format
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

    with open("{}.json".format(empID), 'w') as user_id:
        json.dump({empID: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": empNAME
            } for task in tasks]}, user_id)
