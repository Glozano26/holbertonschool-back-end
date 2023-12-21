#!/usr/bin/python3
""""Using what you did in the task #0, extend your Python script to export
data in the CSV format"""
import requests
import sys
import csv


def employee_todo(employee_id):
    """function that receives the id and query"""
    base_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(base_url)

    data = response.json()
    EMPLOYEE_USERNAME = data.get("username")

    allurl = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(allurl)

    todos = todo_response.json()

    # filename = "{}.csv".format(USER_ID)
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow([employee_id, EMPLOYEE_USERNAME,
                                task['completed'], task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: file and <employee_id>")
    else:
        employee_id = sys.argv[1]
        employee_todo(employee_id)
