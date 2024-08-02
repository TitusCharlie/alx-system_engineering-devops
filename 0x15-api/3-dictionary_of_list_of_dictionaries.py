import json
import requests

# Base URL
base_url = "https://jsonplaceholder.typicode.com"

# Fetch all users
users_response = requests.get(f"{base_url}/users")
users = users_response.json()

# Fetch all tasks
todos_response = requests.get(f"{base_url}/todos")
todos = todos_response.json()

# Organize data into the desired format
data = {}

for user in users:
    user_id = user["id"]
    username = user["username"]
    user_tasks = [
        {
            "username": username,
            "task": todo["title"],
            "completed": todo["completed"]
        }
        for todo in todos if todo["userId"] == user_id
    ]
    data[user_id] = user_tasks

# Export to JSON file
with open("todo_all_employees.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been exported to todo_all_employees.json")

