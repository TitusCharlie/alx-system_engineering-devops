#!/usr/bin/python3
"""
This script uses a REST API to return information about an employee's TODO list progress
and export the data to a JSON file.
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and print the TODO list progress for the given employee ID,
    and export the data to a JSON file.

    Args:
        employee_id (int): The ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user.get('username')

    # Fetch user's todo list
    todos = requests.get(f"{base_url}/todos", params={"userId": employee_id}).json()

    # Print the result
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    # Prepare data for JSON export
    tasks_list = []
    for todo in todos:
        tasks_list.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": employee_name
        })

    tasks_dict = {str(employee_id): tasks_list}

    # Export to JSON
    with open(f"{employee_id}.json", mode='w') as file:
        json.dump(tasks_dict, file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

