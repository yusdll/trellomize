# src/profile_manager.py
from models import Profile, User
from data_manager import DataManager
from logger import Logger

# ProfileManager class to manage profiles
class ProfileManager:
    def __init__(self):
        # initialize the data manager and logger
        self.data_manager = DataManager()
        self.logger = Logger()
    # create a new profile
    def create_profile(self, unique_identifier, title, leader):
        # check the required conditions for providing fields
        if not unique_identifier or not title:
            print("Unique identifier and title are required.")
            return None
        profile = Profile(unique_identifier, title, leader)
        self.data_manager.save_profiles()
        # log the profile creation event
        self.logger.log(f"Profile {title} created by {leader.username}.")
        return profile
    
    # finding users by their username
    def find_user_by_username(self, username):
        return User.find_user_by_username(username)