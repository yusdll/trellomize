# src/user_manager.py
from models import User
from data_manager import DataManager
from logger import Logger

# UserManager class to manage user-related operations
class UserManager:
    def __init__(self):
        # initialize the data manager and logger
        self.data_manager = DataManager()
        self.logger = Logger()
    # Register a new user
    def register_user(self, username, email, password):
        # check the required conditions for providing fields
        if not username or not email or not password:
            print("Username, email, and password are required.")
            return
        # check the existence username already exists
        if User.find_user_by_username(username):
            print("Username already exists.")
            return
            
        user = User(username, email, password)
        self.data_manager.save_user(user)
        self.logger.log(f"User {username} registered.")
        print("User registered successfully.")
        
  # Login a user
    def login(self, username, password):
        # find the user by their username
        user = User.find_user_by_username(username)
        if not user or user.password != password:
            print("Invalid username or password.")
            return None
        # checking the conditions, the activeness of a user
        if not user.is_active:
            print("This account is deactivated.")
            return None
        self.logger.log(f"User {username} logged in.")
        return user