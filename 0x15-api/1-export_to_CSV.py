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

    employeeCSV = empID + '.csv'

    with open(employeeCSV, "w", newline='') as filecsv:
        writer = csv.writer(filecsv, delimiter=',', quoting=csv.QUOTE_ALL)
        for t in tasks:
            writer.writerow([empID, empNAME, t.get('completed'), t.get('title')])
