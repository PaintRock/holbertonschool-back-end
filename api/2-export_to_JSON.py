#!/usr/bin/python3
"""
This module start the conecction with API jsonplace
"""
import requests
from sys import argv
import json


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

    name = user_json[0]['username']
    user_id = user_json[0]['id']
    tasks_list = []
    list_date = []
    
    for date in all_json:
        info = [str(id), name, str(date['completed']), date['title']]
        list_date.append(info)

    for task in all_json:
        task_info = {
            "task": task['title'],
            "completed": task['completed'],
            "username": name
        }
        tasks_list.append(task_info)

    # Export data to JSON
    export_to_json(user_id, tasks_list)


def export_to_json(employee_id, tasks_list):
    file_name = f"{employee_id}.json"
    with open(file_name, 'w') as jsonfile:
        json.dump({str(employee_id): tasks_list}, jsonfile)


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        gather()
