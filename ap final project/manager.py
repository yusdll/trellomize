# src/manager.py
import argparse
from data_manager import DataManager
from models import User

# Function to create an admin user
def create_admin(username, password):
    data_manager = DataManager()
    if data_manager.admin_exists():   # check existence of an admin user
        print("Admin already exists.")
        return

    admin = User(username, "admin@admin.com", password)
    data_manager.save_user(admin)  # save the admin user to the data manager
    print("Admin created successfully.")

# function to purge all data
def purge_data():
    data_manager = DataManager()
    confirmation = input("Are you sure you want to purge all data? This action cannot be undone. (yes/no): ")
    if confirmation.lower() == "yes":
        data_manager.purge_all_data()
        print("All data purged.")
    else:
        print("Purge operation cancelled.")

# Main execution block
if __name__ == "__main__":
    # set up argument parser
    parser = argparse.ArgumentParser(description="Code Management System Manager")
    subparsers = parser.add_subparsers(dest="command")

    # create subparser for creating an admin user
    create_admin_parser = subparsers.add_parser("create-admin")
    create_admin_parser.add_argument("--username", required=True, help="Admin username")
    create_admin_parser.add_argument("--password", required=True, help="Admin password")

    # create subparser for purging all data
    purge_data_parser = subparsers.add_parser("purge-data")

    # parse command-line arguments
    args = parser.parse_args()

    # execute the appropriate command based on user input
    if args.command == "create-admin":
        create_admin(args.username, args.password)
    elif args.command == "purge-data":
        purge_data()
    else:
        parser.print_help()
