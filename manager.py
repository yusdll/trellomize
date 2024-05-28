# src/manager.py
import argparse
from datamanager import DataManager
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Code Management System Manager")
    subparsers = parser.add_subparsers(dest="command")

    create_admin_parser = subparsers.add_parser("create-admin")
    create_admin_parser.add_argument("--username", required=True, help="Admin username")
    create_admin_parser.add_argument("--password", required=True, help="Admin password")

    purge_data_parser = subparsers.add_parser("purge-data")

    args = parser.parse_args()

    if args.command == "create-admin":
        create_admin(args.username, args.password)
    elif args.command == "purge-data":
        purge_data()
    else:
        parser.print_help()
