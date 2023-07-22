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
        
export_to_csv(name, comp, task, list_task)

def export_to_csv(employee_name, completed_tasks, total_tasks, tasks_list):
    """ Chmod done now doument """
    file_name = f"{employee_name.replace(' ', '_')}_todo_list.csv"
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task_title in tasks_list:
            csv_writer.writerow([argv[1], employee_name,
                                 "True" if task_title in completed_tasks else "False", task_title])


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        gather()
