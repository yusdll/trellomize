#src/main.py
from rich.console import Console
from rich.table import Table
from models import User, Profile, Task
from data_manager import DataManager
from user_manager import UserManager
from profile_manager import ProfileManager

console = Console()

def register_user(user_manager):
    print("User Registration")
    username= input ("Enter username: ")
    email = input ("enter email: ")
    password = input ("Enter password: ")
    user_manager.register_user(username, email,password)
    return

def login(user_manager):
    print ("User Login") 
    username = input ("Enter username: ")
    password = input ("Enter password: ")   
    A = user_manager.login(username, password)
    return A

def create_profile(profile_manager):
    print("Create Profile")
    unique_identifier = input("Enter unique identifier: ")
    title = input("Enter profile title: ")
    leader_username = input("Enter leader's username: ")
    leader = User.find_user_by_username(leader_username)
    if leader is None:
        print("Leader not found.")
        return None

    profile = profile_manager.create_profile(unique_identifier, title, leader)
    if profile is None:
        print("Profile creation failed.")
        return None
    else:
        print(f"Profile '{title}' created successfully.")
        return profile
def add_member_to_profile(profile_manager, profile):
    print("Add Member to Profile")
    member_username = input("Enter member's username: ")
    member = User.find_user_by_username(member_username)
    if member is None:
        print("Member not found.")
        return
    profile.add_member(member)
    print(f"Member '{member_username}' added to profile '{profile.title}'.")