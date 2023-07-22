
def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetching employee details
    employee_response = requests.get(f"{base_url}/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetching TODO list for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Counting completed tasks and getting total tasks count
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Displaying results
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo['completed']:
            print("    ", todo['title'])  # Use four spaces for indentation

if __name__ == "__main__":
    try:
        employee_id = int(input("Enter the employee ID: "))
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid input. Please enter an integer for the employee ID.")
