# src/main.py
from user_manager import UserManager
from profile_manager import ProfileManager
from models import User, Profile, Task, Priority, Status

# Function to register a new user
def register_user(user_manager):
    print("User Registration")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    user_manager.register_user(username, email, password)

# Function to log in a user
def login(user_manager):
    print("User Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return user_manager.login(username, password)

# Function to create a new profile
def create_profile(profile_manager, current_user):
    print("Profile Creation")
    title = input("Enter profile title: ")
    unique_identifier = input("Enter unique identifier for the profile: ")
    profile = profile_manager.create_profile(unique_identifier, title, current_user)
    print("Profile created successfully.")
    return profile


# Function to add a member to a profile
def add_member_to_profile(profile_manager, profile):
    print("Adding Member to Profile")
    username = input("Enter username of the user to add: ")
    user = profile_manager.find_user_by_username(username)
    if user:
        profile.add_member(user)
        print(f"{username} added to the profile successfully.")
    else:
        print("User not found.")

# Function to create a new task within a profile
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


# Function to view tasks within a profile
def view_tasks(profile):
    print("Viewing Tasks")
    status_filter = input("Enter task status to filter by (leave empty to view all tasks): ").upper()
    tasks = profile.get_tasks(status_filter)
    for task in tasks:
        print(task)
        
 # Main function to run the code
def main():
    user_manager = UserManager()
    profile_manager = ProfileManager()

    # Load existing users and profiles
    user_manager.data_manager.load_users()
    profile_manager.data_manager.load_profiles()

    current_user = None

    while True:
        print("\Code Management System")
        if not current_user:
            print("1. Register")
            print("2. Login")
            print("9. Exit")
        else:
            print("3. Create Profile")
            print("4. Add Member to Profile")
            print("6. Create Task")
            print("7. View Tasks")
            print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1" and not current_user:
            register_user(user_manager)
        elif choice == "2" and not current_user:
            current_user = login(user_manager)
        elif choice == "3" and current_user:
            create_profile(profile_manager, current_user)
        elif choice == "4" and current_user:
            profile_title = input("Enter profile title to add member to: ")
            profile = Profile.find_profile_by_title(profile_title)
            if profile and profile.leader == current_user:
                add_member_to_profile(profile_manager, profile)
            else:
                print("Profile not found or you are not the leader.")
        elif choice == "6" and current_user:
            profile_title = input("Enter profile title to create task for: ")
            profile = Profile.find_profile_by_title(profile_title)
            if profile and profile.leader == current_user:
                create_task(profile)
            else:
                print("Profile not found or you are not the leader.")
        elif choice == "7" and current_user:
            profile_title = input("Enter profile title to view tasks: ")
            profile = Profile.find_profile_by_title(profile_title)
            if profile:
                view_tasks(profile)
            else:
                print("Profile not found.")
        elif choice == "8" and current_user:
            current_user = None
            print("Logged out.")
        elif choice == "9":
            break
        else:
            print("Invalid choice or you need to login first.")

if __name__ == "__main__":
    main()
     
        
