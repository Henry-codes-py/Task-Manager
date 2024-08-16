# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"  # Standard format for date, (US)

# Check for the existance of the 'tasks.txt' file and create it if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# Read tasks from 'tasks.txt' and store them in a list
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# Function to register a new user
def reg_user(username_password):
    new_username = input("New Username: ")
    if new_username in username_password: # Check for existing username
        print("Username already exists. Please try a different username.")
        return

    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    if new_password != confirm_password: # Confirm passwords match
        print("Passwords do not match")
        return

    print("New user added") # Add the new user
    username_password[new_username] = new_password

    # Update 'user.txt' with the new user list
    with open("user.txt", "w") as out_file:
        for username, password in username_password.items():
            out_file.write(f"{username};{password}\n")

    # Function to add a new task
def add_task(task_list, username_password):
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password:  # check user exists
        print("User does not exist. Please enter a valid username")
        return

    # Collect task details from user input
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    task_due_date = input("Due date of task (YYYY-MM-DD): ")
    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
    curr_date = date.today() # Get current day

    # Create a new task dictionary and add it to the task list
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Update 'tasks.txt' with the new task list
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        for t in task_list:
            task_file.write(f"{t['username']};{t['title']};{t['description']};{t['due_date'].strftime(DATETIME_STRING_FORMAT)};{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if t['completed'] else 'No'}\n")
    print("Task successfully added.")

# Function to allow a user to view there tasks
def view_mine(task_list, curr_user):
    user_tasks = [t for t in task_list if t['username'] == curr_user]  # Filter tasks for the current user
    if not user_tasks:
        print("You have no tasks assigned.")
        return

    # Display tasks and their details
    for i, t in enumerate(user_tasks, start=1):
        status = "Completed" if t['completed'] else "Not Completed"
        print(f"{i}. Task: {t['title']} | Status: {status}\nAssigned to: {t['username']}\nDate Assigned: {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\nDue Date: {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\nTask Description: {t['description']}\n")

    # Allow user to select a task and mark it as completed, or chose to remain uncompleted
    try:
        task_num = int(input("Enter the number of the task you want to select, or '-1' to return to the main menu: "))
        if task_num == -1:
            return
        selected_task = user_tasks[task_num - 1]
    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")
        return

    print(f"You have selected task: {selected_task['title']}")
    action = input("Do you want to mark this task as completed? (yes/no): ").lower()

    if action == 'yes':
        selected_task['completed'] = True
        print(f"Task '{selected_task['title']}' marked as completed.")
        # Update the tasks.txt file with the changed task status
        with open("tasks.txt", "w") as task_file:
            for task in task_list:
                task_file.write(f"{task['username']};{task['title']};{task['description']};{task['due_date'].strftime(DATETIME_STRING_FORMAT)};{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if task['completed'] else 'No'}\n")


    # Placeholder for additional functionality (edit or mark as complete)
    print(f"You have selected task: {selected_task['title']}")
    # Add functionality to edit the task or mark it as complete


with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# establish tasks as a dictionary/key array formation
task_list = []
for t_str in task_data:
    task_components = t_str.split(";")

    # Validate that each task has 6 components
    if len(task_components) == 6:
        curr_t = {}
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False
        task_list.append(curr_t)
    else:
        print(f"Skipping task due to incorrect format: {t_str}")

# Function to generate user overview
def generate_user_overview(task_list, username_password):
    total_users = len(username_password)
    total_tasks = len(task_list)
    current_date = datetime.now().date()

    with open("user_overview.txt", "w") as overview: # Write to view statistics and user ove...
        overview.write(f"Total number of users registered: {total_users}\n")
        overview.write(f"Total number of tasks generated: {total_tasks}\n\n")

        for user in username_password.keys():
            user_tasks = [task for task in task_list if task['username'] == user]
            num_user_tasks = len(user_tasks)
            completed_tasks = len([task for task in user_tasks if task['completed']])
            incomplete_tasks = num_user_tasks - completed_tasks
            overdue_tasks = len([task for task in user_tasks if not task['completed'] and task['due_date'].date() < current_date])

            overview.write(f"User: {user}\n")
            overview.write(f"Total tasks assigned: {num_user_tasks}\n")
            overview.write(f"Percentage of total tasks: {(num_user_tasks / total_tasks * 100) if total_tasks > 0 else 0:.2f}%\n")
            overview.write(f"Percentage of tasks completed: {(completed_tasks / num_user_tasks * 100) if num_user_tasks > 0 else 0:.2f}%\n")
            overview.write(f"Percentage of tasks incomplete: {(incomplete_tasks / num_user_tasks * 100) if num_user_tasks > 0 else 0:.2f}%\n")
            overview.write(f"Percentage of tasks overdue: {(overdue_tasks / num_user_tasks * 100) if num_user_tasks > 0 else 0:.2f}%\n\n")

# Function to generate task overview / report
def generate_task_overview(task_list):
    total_tasks = len(task_list)
    completed_tasks = len([task for task in task_list if task['completed']])
    uncompleted_tasks = total_tasks - completed_tasks
    current_date = datetime.now().date()
    overdue_tasks = len([task for task in task_list if not task['completed'] and task['due_date'].date() < current_date])

    with open("task_overview.txt", "w") as overview:
        overview.write(f"Total number of tasks: {total_tasks}\n")
        overview.write(f"Total number of completed tasks: {completed_tasks}\n")
        overview.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        overview.write(f"Total number of overdue tasks: {overdue_tasks}\n")
        overview.write(f"Percentage of tasks incomplete: {(uncompleted_tasks / total_tasks * 100) if total_tasks > 0 else 0:.2f}%\n")
        overview.write(f"Percentage of tasks overdue: {(overdue_tasks / total_tasks * 100) if total_tasks > 0 else 0:.2f}%\n")



# Login section
# Checks for the existence of 'user.txt' for user credentials, and creates it if it doesn't exist
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# Login loop to authenticate users
logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys(): # Check for user
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass: # check password
        print("Wrong password")
        continue
    else:
        print("Login Successful!") # Break out of the loop upon successful login
        logged_in = True

# Main program loop to present menu options to the user
while True:
    
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
gr - Generate report
e - Exit
: ''').lower() # making sure that the user input is converted to lower case.

    if menu == 'r': # Option to register a new user

        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        new_username = input("New Username: ")

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the passwords are the same 
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

        # - Otherwise throw error.
        else:
            print("Passwords do no match")

    elif menu == 'a': # Option to add a new task
        
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError: # throw error if incorrect format/ expects yyyy-mm-dd
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")


    elif menu == 'va': #option to view all tasks
        
        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            

    elif menu == 'vm': # option for the user or admin to see their current tasks
        view_mine(task_list, curr_user)
        
        for t in task_list:
            if t['username'] == curr_user:
                disp_str = f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)
                
    
    elif menu == 'ds' and curr_user == 'admin': # option for admin to display statistics in terminal
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'gr': # Option to generate report
        generate_task_overview(task_list)
        generate_user_overview(task_list, username_password)


    elif menu == 'e': # Exit the program
        print('Goodbye!!!')
        exit()

    else: # Inform user of error
        print("You have made a wrong choice, Please Try again")