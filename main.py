#src/main.py
from rich.console import Console
from rich.table import Table
from models import User, Profile, Task
from data_manager import DataManager
from user_manager import UserManager
from profile_manager import ProfileManager

console = Console()

def register_user(user_manager):
    print("User Registration")
    username= input ("Enter username: ")
    email = input ("enter email: ")
    password = input ("Enter password: ")
    user_manager.register_user(username, email,password)
    return

def login(user_manager):
    print ("User Login") 
    username = input ("Enter username: ")
    password = input ("Enter password: ")   
    A = user_manager.login(username, password)
    return A

def create_profile(profile_manager):
    print("Create Profile")
    unique_identifier = input("Enter unique identifier: ")
    title = input("Enter profile title: ")
    leader_username = input("Enter leader's username: ")
    leader = User.find_user_by_username(leader_username)
    if leader is None:
        print("Leader not found.")
        return None

    profile = profile_manager.create_profile(unique_identifier, title, leader)
    if profile is None:
        print("Profile creation failed.")
        return None
    else:
        print(f"Profile '{title}' created successfully.")
        return profile

def add_member_to_profile(profile_manager, profile):
    print("Add Member to Profile")
    member_username = input("Enter member's username: ")
    member = User.find_user_by_username(member_username)
    if member is None:
        print("Member not found.")
        return
    profile.add_member(member)
    print(f"Member '{member_username}' added to profile '{profile.title}'.")

def create_task(profile_manager, profile):
    print("Create Task")
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    assignees = input("Enter assignees (comma-separated): ")
    assignees = [assignee.strip() for assignee in assignees.split(",")]
    task = Task(task_title, task_description, assignees)
    profile.add_task(task)
    print(f"Task '{task_title}' created for profile '{profile.title}'.")

def view_tasks(profile_manager, profile):
    print("View Tasks")
    tasks = profile.get_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"Task '{task.title}' - Status: {task.status.name}")

        def main():
    data_manager = DataManager()
    if not data_manager.admin_exists():
        console.print("[bold green]Creating admin user...[/bold green]")
        admin = User("admin", "admin@example.com", "password")
        data_manager.save_user(admin)

    while True:
        console.print("[bold green]Welcome to the Task Manager![/bold green]")
        console.print("[bold]Please select an option:[/bold]")
        console.print("1. Register")
        console.print("2. Login")
        console.print("3. Create Profile")
        console.print("4. Add Member to Profile")
        console.print("5. Create Task")
        console.print("6. View Tasks")
        console.print("7. Create Admin")
        console.print("8. Purge Data")
        console.print("9. Exit")

        choice = console.input("[bold]Enter your choice (1-9): [/bold]")

        if choice == "1":
            register_user(UserManager())
        elif choice == "2":
            user = login(UserManager())
            if user:
                console.print(f"[bold green]Logged in as {user.username}[/bold green]")
                while True:
                    console.print(f"[bold green]Logged in as {user.username}[/bold green]")
                    console.print("[bold]Please select an option:[/bold]")
                    console.print("1. Create Profile")
                    console.print("2. Add Member to Profile")
                    console.print("3. Create Task")
                    console.print("4. View Tasks")
                    console.print("5. Logout")

                    choice = console.input("[bold]Enter your choice (1-5): [/bold]")

                    if choice == "1":
                        profile = create_profile(ProfileManager())
                        if profile:
                            create_task(ProfileManager(), profile)
                    elif choice == "2":
                        profile = create_profile(ProfileManager())
                        if profile:
                            add_member_to_profile(ProfileManager(), profile)
                    elif choice == "3":
                        profile = create_profile(ProfileManager())
                        if profile:
                            create_task(ProfileManager(), profile)
                    elif choice == "4":
                        profile = create_profile(ProfileManager())
                        if profile:
                            view_tasks(ProfileManager(), profile)
                    elif choice == "5":
                        console.print("[bold green]Logged out[/bold green]")
                        break
                    else:
                        console.print("[bold red]Invalid choice. Please try again.[/bold red]")
        elif choice == "3":
            create_profile(ProfileManager())
        elif choice == "4":
            profile = create_profile(ProfileManager())
            if profile:
                add_member_to_profile(ProfileManager(), profile)
        elif choice == "5":
            profile = create_profile(ProfileManager())
            if profile:
                create_task(ProfileManager(), profile)
        elif choice == "6":
            profile = create_profile(ProfileManager())
            if profile:
                view_tasks(ProfileManager(), profile)
        elif choice == "7":
            create_admin("admin", "password")
        elif choice == "8":
            purge_data()
        elif choice == "9":
            console.print("[bold green]Exiting Task Manager. Goodbye![/bold green]")
            break
        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")

if __name__ == "__main__":
    main()