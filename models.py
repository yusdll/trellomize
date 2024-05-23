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