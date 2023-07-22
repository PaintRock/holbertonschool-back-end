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
    list_date = []

    for dates in all_json:
        info = [str(id), name, str(date['completed']), date['title']]
        list_date.append(info)

    name = user_json[0]['name']

    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(list_date)


if __name__ == '__main__':
    gather()
