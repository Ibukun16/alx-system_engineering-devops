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
    USER_ID = argv[1]
    baseURL = 'https://jsonplaceholder.typicode.com/users'
    empURL = baseURL + '/' + USER_ID
    todoURL = empURL + '/todos'

    responsename = sessionquest.get(empURL)
    userNAME = responsename.json()['username']

    responsetodo = sessionquest.get(todoURL)
    tasks = responsetodo.json()

    completeTasks = []
    dictionary = {}

    for task in tasks:
        completeTasks.append(
                {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": userNAME,
                })
    dictionary[USER_ID] = completeTasks
    jsonfile = USER_ID + ".json"
    with open(jsonfile, 'w') as filename:
        json.dump(dictionary, filename)
