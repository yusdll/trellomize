# src/models.py
import uuid
from datetime import datetime, timedelta
from enum import Enum

class Priority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

class Status(Enum):
    BACKLOG = 1
    TODO = 2
    DOING = 3
    DONE = 4
    ARCHIVED = 5

class User:
    users = []

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = True
        User.users.append(self)

    @classmethod
    def find_user_by_username(cls, username):
        for user in cls.users:
            if user.username == username:
                return user
        return None
class Profile:
    profiles = []

    def __init__(self, unique_identifier, title, leader):
        self.unique_identifier = unique_identifier
        self.title = title
        self.leader = leader
        self.members = []
        self.tasks = []
        Profile.profiles.append(self)

    def add_member(self, user):
        if user not in self.members:
            self.members.append(user)

    def remove_member(self, user):
        if user in self.members:
            self.members.remove(user)

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self, status_filter=None):
        if status_filter:
            return [task for task in self.tasks if task.status.name == status_filter]
        return self.tasks

    @classmethod
    def find_profile_by_title(cls, title):
        for profile in cls.profiles:
            if profile.title == title:
                return profile
        return None

class Task:
    def __init__(self, title, description, assignees):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=24)
        self.assignees = assignees
        self.priority = Priority.LOW
        self.status = Status.BACKLOG
        self.log = []
        self.comments = []

    def update_priority(self, priority):
        self.priority = priority
        self.log_change("priority", priority.name)

    def update_status(self, status):
        self.status = status
        self.log_change("status", status.name)

    def log_change(self, field, value):
        self.log.append({
            "field": field,
            "value": value,
            "timestamp": datetime.now().isoformat()
        })

    def add_comment(self, user, content):
        self.comments.append((user.username, content, datetime.now()))