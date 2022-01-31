#!usr/bin/python3
import json
import requests
import sys

"""
This script stores the information of all the employee
and his/her TODO LIST PROGRESS in a JSON file
"""


def infoToJson():

    i = int(sys.argv[1])
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    TASK_COMPLETED_STATUS = []
    filename = "{}.json".format(i)
    val_repr = {}
    val_list = []
    obj = {}
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    usr = requests.get('https://jsonplaceholder.typicode.com/users/' + str(i))
    USERNAME = usr.json().get('username')
    for todo in todos.json():
        TASK_COMPLETED_STATUS.append(todo.get('completed'))
        TASK_TITLE.append(todo.get('title'))
    for status, task in zip(TASK_COMPLETED_STATUS, TASK_TITLE):
        val_list.append({"task": task, "completed": status,
                         "username": USERNAME})
    with open(filename, "w") as jsonfile:
        json.dump({i: val_list}, jsonfile)


if __name__ == "__main__":
    infoToJson()
