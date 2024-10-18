#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee.
    
    Args:
        employee_id (int): The ID of the employee whose TODO list progress will be fetched.
    
    The function prints the following information to the console:
        - Employee's name and the number of completed tasks out of the total tasks.
        - The titles of the completed tasks, each preceded by a tab and a space.
    
    Raises:
        ValueError: If employee_id is not an integer.
    """
    # Define the API endpoints for the user and the todos
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    
    # Make a request to get employee details
    user_response = requests.get(user_url)
    # Make a request to get the employee's TODO list
    todos_response = requests.get(todos_url)
    
    # Check if the API response is successful for both requests
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return
    
    # Parse the JSON response into Python data structures
    user_data = user_response.json()
    todos_data = todos_response.json()
    
    # Extract the employee's name
    employee_name = user_data.get('name')
    
    # Calculate the total number of tasks and completed tasks
    t
