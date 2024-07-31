#!/usr/bin/python3
"""A script that build on the previous task which uses REST API
to obtain information about an employee TODO list then export the
data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    userID = argv[1]
    baseURL = 'https://jsonplaceholder.typicode.com/users'
    userNAME = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(userID)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1])).json()

    with open("{}.json".format(userID), "w") as USER_ID:
        json.dump({userID: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": userNAME.get('username')
            } for task in tasks]}, USER_ID)
