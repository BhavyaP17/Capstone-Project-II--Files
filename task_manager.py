# Capstone Project II : Submitted by Bhavya Patteeswaran

# =====importing libraries===========
from datetime import datetime

# ====Login Section====
# Read the user.txt file for usernames and password.
with open("user.txt", "r") as file:
    login = file.readlines()

    # use list to store the usernames and passwords from file
    usernames_lst = []
    passwords_lst = []
    for line in login:
        login_details = line.split(', ')
        usernames_lst.append(login_details[0])
        passwords_lst.append(login_details[1].strip("\n"))
    # Input the username and password. use while loop to validate te username and password.
    print("'Login to the task manager website'")

    username_in = input("Enter your username: ")
    Login_invalid = True
    while Login_invalid:
        if username_in not in usernames_lst:
            print("The username is incorrect.")
            username_in = input("Enter your username: ")
        else:
            print("The username is correct.")
            password_in = input("Enter your password: ")
            password_invalid = True
            while password_invalid:
                if password_in not in passwords_lst:
                    print("Your username is correct but your password is incorrect.")
                    password_in = input("Enter your password: ")
                else:
                    print("Your password is correct. Login is successful")
                    password_invalid = False
            Login_invalid = False

while True:
    menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':  # Only the user logged in as 'admin', will be able to add new users.
        if username_in != "admin":
            print("You are not an admin user, only admin can register new users.")

        else:
            # Create a new menu to display for admin only.
            admin_menu = (input("""
Please select one of the following options:
                r - register a new user
                d - display statistics i.e. Total number of tasks & users are displayed
                : """))
            if admin_menu == "r":
                new_user = (input("Please enter a new user name: "))
                new_user_password = (input("Please enter a new password: "))

                new_password = True
                while new_password:
                    confirm_new_password = input("Please retype your password to confirm: ")
                    if new_user_password == confirm_new_password:
                        print("Your passwords are match.")
                    else:
                        print("Your passwords do not match!")
                    new_password = False

                with open('user.txt', 'a') as user_file:
                    user_file.write(f"\n{new_user}, {new_user_password}")

            elif admin_menu == "d":  # display statistics
                tasks_num = 0
                users_num = 0

                with open("tasks.txt", "r") as task_file:
                    for line in task_file:
                        tasks_num += 1
                print(f"\nTotal number of tasks: {tasks_num}")

                with open("user.txt", "r") as username:
                    for line in username:
                        users_num += 1
                print(f"Total number of users: {users_num}")

            else:
                print("Select the valid option, try again from main menu")

    elif menu == 'a':  # add a new task to task.txt file
        with open("tasks.txt", "a+") as task_file:
            today = datetime.today()
            new_task_username = input("Enter the 'username' of the person whom the task is assigned to: ")
            new_title = input("Enter the 'title' of the new task: ")
            new_description = input("Enter the 'description' of the new task: ")
            new_assigned_date = today.strftime("%d %b %Y")
            new_due_date = input("Enter the due date of the new task in the format: dd mmm yyyy: ")
            task_completed = "No"

            task_file.write(
                f"\n{new_task_username}, {new_title}, {new_description}, {new_assigned_date}, {new_due_date}, {task_completed}")
            print("The new task is added to the tasks.txt file")

    elif menu == 'va':  # view all tasks
        with open("tasks.txt", "r") as tasks_read:
            data = tasks_read.readlines()
            for pos, line in enumerate(data, start=1):
                split_data = line.split(", ")

                output = f'--------------------[{pos}]-------------------------------\n'
                output += '\n'
                output += f'Task: \t\t\t{split_data[1]}\n'
                output += f'Assigned to: \t{split_data[0]}\n'
                output += f'Assigned Date:\t{split_data[3]}\n'
                output += f'Due Date:\t\t{split_data[4]}\n'
                output += f'Is completed?:  {split_data[5]}\n'
                output += f'Description: \t{split_data[2]}\n'
                output += '\n'
                output += '------------------------------------------------------\n'

                print(output)

    elif menu == 'vm':  # only view the task assigned to a user
        with open("tasks.txt", "r") as tasks_read:
            data = tasks_read.readlines()
            for pos, line in enumerate(data, start=1):
                split_data = line.split(", ")

                if username_in == split_data[0]:
                    output = f'--------------------[{pos}]-------------------------------\n'
                    output += '\n'
                    output += f'Task: \t\t\t{split_data[1]}\n'
                    output += f'Assigned to: \t{split_data[0]}\n'
                    output += f'Assigned Date:\t{split_data[3]}\n'
                    output += f'Due Date:\t\t{split_data[4]}\n'
                    output += f'Is completed?:  {split_data[5]}\n'
                    output += f'Description: \t{split_data[2]}\n'
                    output += '\n'
                    output += '------------------------------------------------------\n'

                    print(output)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
