#!/usr/bin/python3
"""
REST GET
"""
import requests
from sys import argv

if __name__ == "__main__":

    employee_ID = argv[1]
    complited = 0
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_ID)).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            employee_ID)).json()
    for task in todos:
        if task['completed'] is True:
            complited += 1
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user['name'], complited, len(todos)))
    for task in todos:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
