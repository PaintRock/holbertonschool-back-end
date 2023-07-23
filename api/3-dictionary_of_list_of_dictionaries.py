#!/usr/bin/python3
"""
This module start the conecction with API jsonplace
"""
import json
import requests
from sys import argv


def gather():
    """
    This method retrieves all tasks from all
    employees and exports the data in JSON format.
    """

    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    users_json = response_users.json()
    todos_json = response_todos.json()

    tasks_by_employee = {}

    for user in users_json:
        user_id = user['id']
        user_name = user['username']
        tasks_by_employee[user_id] = []

    for todo in todos_json:
        user_id = todo['userId']
        task_info = {
            "username": users_json[user_id-1]['username'],
            "task": todo['title'],
            "completed": todo['completed']
        }
        tasks_by_employee[user_id].append(task_info)

    # Export data to JSON
    export_to_json(tasks_by_employee)


def export_to_json(data):
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == '__main__':
    gather()
