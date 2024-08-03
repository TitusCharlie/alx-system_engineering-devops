#!/usr/bin/python3
"""
check and return TODO list progress
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and print the TODO list progress for the given employee ID.

    Args:
        employee_id (int): The ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"
    todos_count = 0
    todos_done = 0
    titles = []

    # Fetch user information
    user = requests.get(f"{base_url}/users").json()
    employee_name = None
    for i in user:
        if i.get('id') == employee_id:
            employee_name = i['name']

    # Fetch user's todo list
    todos = requests.get(f"{base_url}/todos").json()
    for i in todos:
        if i.get('userId') == employee_id:
            if i.get('completed') is True:
                titles.append(i['title'])
                todos_done += 1
            todos_count += 1

    # Print the result
    print(f"Employee {employee_name} is done with tasks({todos_done}/{todos_count}):")
    for title in titles:
        print(f"\t {title}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
