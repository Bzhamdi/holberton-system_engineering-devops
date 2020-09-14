#!/usr/bin/python3
"""
REST GET
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users"
                         ).json()
    to_json = {}
    for user in users:
        employee_ID = user["id"]
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(
                                employee_ID)).json()
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'
            .format(
                employee_ID)).json()

        tasks = []

        to_json[employee_ID] = tasks

        for x in todos:
            dic = {}
            dic["task"] = x['title']
            dic["completed"] = x['completed']
            dic["username"] = user['username']
            tasks.append(dic)
    with open("todo_all_employees.json", 'w') as file:
        json.dump(to_json, file)
