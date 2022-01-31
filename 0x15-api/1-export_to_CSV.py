#!usr/bin/python3
import csv
import requests
import sys

"""
This script using the REST API provided returns fr a given
employee ID, information about his/her TODO LIST PROGRESS
"""


def infoToCsv():

    i = int(sys.argv[1])
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    TASK_COMPLETED_STATUS = []
    tmp_str = ""
    filename = "{}.csv".format(i)
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    usr = requests.get('https://jsonplaceholder.typicode.com/users/' + str(i))
    USERNAME = usr.json().get('username')
    for todo in todos.json():
        TASK_COMPLETED_STATUS.append(todo.get('completed'))
        TASK_TITLE.append(todo.get('title'))
    
    with open(filename, 'w') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames,
                                quoting = csv.QUOTE_ALL)
        for status, task in zip(TASK_COMPLETED_STATUS, TASK_TITLE):
            writer.writerow({"USER_ID":i, "USERNAME": USERNAME,
                            "TASK_COMPLETED_STATUS":status,
                            "TASK_TITLE": task})


if __name__ == "__main__":
    infoToCsv()
