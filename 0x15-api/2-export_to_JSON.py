#!/usr/bin/python3
"""
REST GET
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    employee_ID = argv[1]

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(
                            employee_ID)).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(
            employee_ID)).json()

    tasks = []
    to_json = {}
    to_json[employee_ID] = tasks
    with open("{}.json".format(employee_ID), 'w') as file:
        for x in todos:
            dic = {}
            dic["task"] = x['title']
            dic["completed"] = x['completed']
            dic["username"] = user['username']
            tasks.append(dic)

        json.dump(to_json, file)
