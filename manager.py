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

    def purge_data():
    data_manager = DataManager()
    confirmation = input("Are you sure you want to purge all data? This action cannot be undone. (yes/no): ")
    if confirmation.lower() == "yes":
        data_manager.purge_all_data()
        print("All data purged.")
    else:
        print("Purge operation cancelled.")