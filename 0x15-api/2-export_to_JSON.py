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
    userID = argv[1]
    baseURL = 'https://jsonplaceholder.typicode.com/users'
    empURL = baseURL + '/' + userID
    todoURL = empURL + '/todos'

    responsename = sessionquest.get(empURL)
    userNAME = responsename.json()['name']

    responsetodo = sessionquest.get(todoURL)
    tasks = responsetodo.json()

    with open("{}.json".format(userID), 'w') as user_id:
        json.dump({userID: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": userNAME
            } for task in tasks]}, user_id)
