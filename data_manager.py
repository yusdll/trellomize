# src/data_manager.py
import json
import os
from models import User, Profile, Task, datetime, Priority, Status

# DataManager class to handle data persistence
class DataManager:
    def __init__(self):
        self.user_file = "users.json" # store user data
        self.profile_file = "profiles.json" #store profile data


    def save_user(self, user):
        users = self.load_data(self.user_file)
        # append the new user data to the list
        users.append({
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "is_active": user.is_active
        })
        self.save_data(self.user_file, users)

    # Loading users from the user file
    def load_users(self):
        users = self.load_data(self.user_file)
        # create user objects from the loaded data and add them to specified file
        for user_data in users:
            user = User(user_data["username"], user_data["email"], user_data["password"])
            user.is_active = user_data["is_active"]
        return User.users

        def save_profiles(self):
        profiles = [] # store profile data by creating a list
        # iterate over the specified list and convert each profile to a dictionary
        for profile in Profile.profiles:
        for profile in Profile.profiles:
            profiles.append({
                "unique_identifier": profile.unique_identifier,
                "title": profile.title,
                "leader": profile.leader.username,
                "members": [member.username for member in profile.members],
                "tasks": [{
                    "id": task.id,
                    "title": task.title,
                    "description": task.description,
                    "start_time": task.start_time.isoformat(),
                    "end_time": task.end_time.isoformat(),
                    "assignees": [user.username for user in task.assignees],
                    "priority": task.priority.name,
                    "status": task.status.name,
                    "log": task.log,
                    "comments": [(comment[0], comment[1], comment[2].isoformat()) for comment in task.comments]
                } for task in profile.tasks]
            })
        self.save_data(self.profile_file, profiles)

    # Load profiles from the profile file
    def load_profiles(self):
        profiles = self.load_data(self.profile_file)
        
        # create Profile objects from the loaded data
        for profile_data in profiles:
            leader = User.find_user_by_username(profile_data["leader"])
            profile = Profile(profile_data["unique_identifier"], profile_data["title"], leader)
            # add members to the profile
            for member_username in profile_data["members"]:
                user = User.find_user_by_username(member_username)
                profile.add_member(user)
            # add tasks to the profile
            for task_data in profile_data["tasks"]:
                assignees = [User.find_user_by_username(username) for username in task_data["assignees"]]
                task = Task(task_data["title"], task_data["description"], assignees)
                task.id = task_data["id"]
                task.start_time = datetime.fromisoformat(task_data["start_time"])
                task.end_time = datetime.fromisoformat(task_data["end_time"])
                task.priority = Priority[task_data["priority"]]
                task.status = Status[task_data["status"]]
                task.log = task_data["log"]
                task.comments = [(comment[0], comment[1], datetime.fromisoformat(comment[2])) for comment in task_data["comments"]]
                profile.add_task(task)
        return Profile.profiles

    def load_data(self, file):
        if os.path.exists(file):
            with open(file, 'r') as f:
                return json.load(f)
        return []

    def save_data(self, file, data):
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)

    def admin_exists(self):
        users = self.load_data(self.user_file)
        return any(user["username"] == "admin" for user in users)

    def purge_all_data(self):
        if os.path.exists(self.user_file):
            os.remove(self.user_file)
        if os.path.exists(self.profile_file):
            os.remove(self.profile_file)
