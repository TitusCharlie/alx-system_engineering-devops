#!/usr/bin/python3
"""
This script uses a REST API to return information about an employee's TODO list progress
and export the data to a CSV file.
"""
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and print the TODO list progress for the given employee ID.

    Args:
        employee_id (int): The ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user.get('username')

    # Fetch user's todo list
    todos = requests.get(f"{base_url}/todos", params={"userId": employee_id}).json()

    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the result
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    # Export to CSV
    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, employee_name, todo.get('completed'), todo.get('title')])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

