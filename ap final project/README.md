# trellomize
Code Management System
This README provides an overview of the Code Management System, detailing its components, functionalities, and usage instructions.
Components

    Models:
        Contains classes for User, Profile, and Task with attributes and methods for managing users, profiles, and tasks.
    Profile Manager:
        Manages profiles, including creation, member addition, and task assignment.
    User Manager:
        Handles user-related operations such as user registration and login.
    Data Manager:
        Manages data persistence by saving and loading user and profile data to/from JSON files.
    Logger:
        Provides logging functionality to track events and actions within the system.
    Manager:
        Main script for creating an admin user and purging all data.
    Main:
        Core functionality script for user interaction, profile, and task management.
    Tests:
        Unit tests for ensuring the functionality and integrity of the system.

Functionality

    User Management:
        Register new users, login, and handle user data.
    Profile Management:
        Create profiles, add members, and assign tasks within profiles.
    Task Management:
        Create tasks with titles, descriptions, assignees, priorities, and statuses.
    Data Persistence:
        Save and load user and profile data to ensure data integrity.
    Logging:
        Log events such as user registration, profile creation, and task updates.

Usage

    Setup:
        Ensure Python 3.8 or higher is installed.
        Install any required dependencies.
    Execution:
        Run main.py to interact with the system.
        Use manager.py for admin user creation and data purging.
        Execute test.py to run unit tests.
    Contributing:
        Fork the repository, make changes, and submit pull requests for enhancements.
    License:
        This project is licensed under the MIT License.
