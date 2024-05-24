# src/manager.py
import argparse
from data_manager import DataManager
from models import User

def create_admin(username, password):
    data_manager = DataManager()
    if data_manager.admin_exists():
        print("Admin already exists.")
        return
    admin = User(username, "admin@admin.com", password)
    data_manager.save_user(admin)
    print("Admin created successfully.")