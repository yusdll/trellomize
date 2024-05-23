# src/data_manager.py
import json
import os
from models import User, Profile

class DataManager:
    def __init__(self):
        self.user_file = "users.json"
        self.profile_file = "profiles.json"

    def save_user(self, user):
        users = self.load_data(self.user_file)
        users.append({
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "is_active": user.is_active
        })
        self.save_data(self.user_file, users)

    def load_users(self):
        users = self.load_data(self.user_file)
        for user_data in users:
            user = User(user_data["username"], user_data["email"], user_data["password"])
            user.is_active = user_data["is_active"]
        return User.users

    def save_profiles(self):
        profiles = []
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
