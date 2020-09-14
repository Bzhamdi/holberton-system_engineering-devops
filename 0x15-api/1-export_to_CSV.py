#!/usr/bin/python3
"""
REST GET
"""
import requests
from sys import argv
import csv

if __name__ == "__main__":

    employee_ID = argv[1]
    
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(
                            employee_ID)).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(
            employee_ID)).json()

    with open("{}.csv".format(employee_ID), 'w') as file:
        t_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            t_writer.writerow([int(employee_ID), user['username'],
                               task['completed'],
                               task['title']])
