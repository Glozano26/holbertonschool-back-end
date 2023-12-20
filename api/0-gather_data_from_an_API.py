#!/usr/bin/python3

import requests
import sys



def employee_todo(employee_id):
    base_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(base_url)
    

    data = response.json()
    EMPLOYEE_NAME = data.get("name")
    EMPLOYEE_USERNAME = data.get("username")

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    

    todos = todo_response.json()
    NUMBER_OF_DONE_TASKS = []
    for task in todos:
        if task['completed']:
            NUMBER_OF_DONE_TASKS.append(task)
    TOTAL_NUMBER_OF_TASKS = len(todos)

    print(f"Employee {EMPLOYEE_NAME} is done with tasks "
          f"({len(NUMBER_OF_DONE_TASKS)}/{TOTAL_NUMBER_OF_TASKS}):")

    for TASK_TITLE in NUMBER_OF_DONE_TASKS:
        print(f"\t{TASK_TITLE['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        employee_todo(employee_id)