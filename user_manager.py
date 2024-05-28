# src/user_manager.py
from models import User
from data_manager import DataManager
from logger import Logger

class UserManager:
    def __init__(self):
        self.data_manager = DataManager()
        self.logger = Logger()

    def register_user(self, username, email, password):
        if not username or not email or not password:
            print("Username, email, and password are required.")
            return
        if User.find_user_by_username(username):
            print("Username already exists.")
            return
        user = User(username, email, password)
        self.data_manager.save_user(user)
        self.logger.log(f"User {username} registered.")
        print("User registered successfully.")

    def login(self, username, password):
        user = User.find_user_by_username(username)
        if not user or user.password != password:
            print("Invalid username or password.")
            return None
        if not user.is_active:
            print("This account is deactivated.")
            return None
        self.logger.log(f"User {username} logged in.")
        return user