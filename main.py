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
