#!usr/bin/python3
import requests
import sys

"""
This script using the REST API provided returns fr a given
employee ID, information about his/her TODO LIST PROGRESS
"""


def infoToJson():

    i = int(sys.argv[1])
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    TASK_COMPLETED_STATUS = []
    tmp_str = ""
    json_repr = dict()
    val_repr = {}
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    usr = requests.get('https://jsonplaceholder.typicode.com/users/' + str(i))
    USERNAME = usr.json().get('username')
    for todo in todos.json():
        TASK_COMPLETED_STATUS.append(todo.get('completed'))
        TASK_TITLE.append(todo.get('title'))
    for status, task in zip(TASK_COMPLETED_STATUS, TASK_TITLE):
        with open(str(id) + ".json", w) as fin:
            tmp = "{},{},{},{}\n".format(i, USERNAME, status, task)
            val_repr['task'] = task
            val_repr['completed'] = status
            val_repr['username'] = USERNAME
            json_repr[str(i)] = list(val_repr)
            fin.write(json_repr)


if __name__ == "__main__":
    infoToJson()
