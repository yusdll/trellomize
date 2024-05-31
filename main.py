# src/main.py
from user_manager import UserManager
from profile_manager import ProfileManager
from models import User, Profile, Task, Priority, Status

def register_user(user_manager):
    print("User Registration")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    user_manager.register_user(username, email, password)

def login(user_manager):
    print("User Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return user_manager.login(username, password)

def create_profile(profile_manager, current_user):
    print("Profile Creation")
    title = input("Enter profile title: ")
    unique_identifier = input("Enter unique identifier for the profile: ")
    profile = profile_manager.create_profile(unique_identifier, title, current_user)
    print("Profile created successfully.")
    return profile



def add_member_to_profile(profile_manager, profile):
    print("Adding Member to Profile")
    username = input("Enter username of the user to add: ")
    user = profile_manager.find_user_by_username(username)
    if user:
        profile.add_member(user)
        print(f"{username} added to the profile successfully.")
    else:
        print("User not found.")

def create_task(profile):
    print("Task Creation")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    assignees = input("Enter assignees (comma-separated usernames): ").split(',')
    assignee_objects = [User.find_user_by_username(username.strip()) for username in assignees]
    task = Task(title, description, assignee_objects)
    priority = input("Enter task priority (CRITICAL, HIGH, MEDIUM, LOW): ").upper()
    task.update_priority(Priority[priority])
    status = input("Enter task status (BACKLOG, TODO, DOING, DONE, ARCHIVED): ").upper()
    task.update_status(Status[status])
    profile.add_task(task)
    print("Task created successfully.")


def view_tasks(profile):
    print("Viewing Tasks")
    status_filter = input("Enter task status to filter by (leave empty to view all tasks): ").upper()
    tasks = profile.get_tasks(status_filter)
    for task in tasks:
        print(task)
