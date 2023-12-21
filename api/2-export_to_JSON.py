#!/usr/bin/python3
""""Using what you did in the task #0, extend your Python script to export
data in the CSV format"""
import csv
import json
import requests
import sys


def employee_todo(employee_id):
    """function that receives the id and query"""
    base_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(base_url)

    user_data = response.json()
    EMPLOYEE_USERNAME = user_data.get("username")

    allurl = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(allurl)

    todos = todo_response.json()

    datas_exported = []
    for task in todos:
        data_to_export = {
            "task": task["title"],
            "completed": task["completed"],
            "username": EMPLOYEE_USERNAME
        }
        datas_exported.append(data_to_export)

    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump({f"{employee_id}": datas_exported}, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: file and <employee_id>")
    else:
        employee_id = sys.argv[1]
        employee_todo(employee_id)
