#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee data
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    
    # Check if responses are valid
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return
    
    user_data = user_response.json()
    todos_data = todos_response.json()
    
    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    
    number_of_done_tasks = len(completed_tasks)

    # Display the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    
    # Display titles of completed tasks
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == '__main__':
    # Ensure the script accepts an integer as a parameter
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
