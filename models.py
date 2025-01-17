# src/models.py
import uuid
from datetime import datetime, timedelta
from enum import Enum

# Define the priority levels for tasks
class Priority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

# Define the status levels for tasks
class Status(Enum):
    BACKLOG = 1
    TODO = 2
    DOING = 3
    DONE = 4
    ARCHIVED = 5

# Represent a user in the system by user class
class User:


    # list to store all users
    users = []

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = True
        # add specified user to the list of users
        User.users.append(self)

    # method of finding users by their name
    @classmethod
    def find_user_by_username(cls, username):
        for user in cls.users:
            if user.username == username:
                return user
        return None

    
class Profile:

     # list to store all profiles
    profiles = []

    def __init__(self, unique_identifier, title, leader):
        self.unique_identifier = unique_identifier
        self.title = title
        self.leader = leader
        self.members = []
        self.tasks = []

        # add the profile to the list of profiles
        Profile.profiles.append(self)

    # Add a member to the profile
    def add_member(self, user):
        if user not in self.members:
            self.members.append(user)

    # Remove a member from the profile
    def remove_member(self, user):
        if user in self.members:
            self.members.remove(user)

    def add_task(self, task):
        self.tasks.append(task)

    # Get the tasks for the profile, optionally filtered by status
    def get_tasks(self, status_filter=None):
        if status_filter:
            return [task for task in self.tasks if task.status.name == status_filter]
        return self.tasks


    # method of finding a profile by its title
    @classmethod
    def find_profile_by_title(cls, title):
        for profile in cls.profiles:
            if profile.title == title:
                return profile
        return None

# Task class to represent a task in the system
class Task:
    def __init__(self, title, description, assignees):
        self.id = str(uuid.uuid4()) # generate a unique identifier for the task
        self.title = title
        self.description = description
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=24)  # set the default end time to 24 hours from now
        self.assignees = assignees
        self.priority = Priority.LOW # set the default priority to low
        self.status = Status.BACKLOG # set the default status backlog
        self.log = [] # list to store the task's change log
        self.comments = [] # list to store the task's comments

    # update the priority of the task and log the change
    def update_priority(self, priority):
        self.priority = priority
        self.log_change("priority", priority.name)
    # update the status of the task and log the change
    def update_status(self, status):
        self.status = status
        self.log_change("status", status.name)

    # log a change to the task
    def log_change(self, field, value):
        self.log.append({
            "field": field,
            "value": value,
            "timestamp": datetime.now().isoformat()
        })

    def add_comment(self, user, content):
        self.comments.append((user.username, content, datetime.now()))
