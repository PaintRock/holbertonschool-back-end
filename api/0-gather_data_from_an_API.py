#!/usr/bin/python3
"""
This module start the conecction with API jsonplace
"""
import requests
from sys import argv


def gather():
    """
    This methos return the tasks of the users
    """

    url_all = "https://jsonplaceholder.typicode.com/todos?"
    url_user = "https://jsonplaceholder.typicode.com/users?"
    argv_all = {'userId': argv[1]}
    argv_user = {'id': argv[1]}

    response_all = requests.get(url_all, params=argv_all)
    response_user = requests.get(url_user, params=argv_user)

    all_json = response_all.json()
    user_json = response_user.json()
    comp, task = 0, 0
    list_task = []

    for dates in all_json:
        task += 1
        if dates['completed']:
            comp += 1
            list_task.append(dates['title'])

    name = user_json[0]['name']
    print("Employee {} is done with tasks({}/{}):".format(name, comp, task))
    for task in list_task:
        print("\t " + task)


if __name__ == '__main__':
    gather()
