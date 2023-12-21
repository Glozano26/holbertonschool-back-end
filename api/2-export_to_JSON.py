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

    data_to_export = {
        "USER_ID": [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": EMPLOYEE_USERNAME
            }
            for task in todos
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump(data_to_export, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: file and <employee_id>")
    else:
        employee_id = sys.argv[1]
        employee_todo(employee_id)
