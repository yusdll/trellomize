import unittest
from models import User, Profile, Task, Priority, Status

class TestCodeManagementSystem(unittest.TestCase):

    def setUp(self):
        User.users = []
        Profile.profiles = []

    def test_user_registration(self):
        user = User("testuser", "testuser@example.com", "password")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.password, "password")


    def test_profile_creation(self):
        user = User("leader", "leader@example.com", "password")
        profile = Profile("1", "Test Profile", user)
        self.assertEqual(profile.unique_identifier, "1")
        self.assertEqual(profile.title, "Test Profile")
        self.assertEqual(profile.leader, user)
        self.assertIn(user, profile.members)

    def test_task_creation(self):
        user = User("assignee", "assignee@example.com", "password")
        task = Task("Test Task", "Description", [user])
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Description")
        self.assertIn(user, task.assignees)
        self.assertEqual(task.priority, Priority.LOW)
        self.assertEqual(task.status, Status.BACKLOG)

    def test_profile_add_member(self):
        leader = User("leader", "leader@example.com", "password")
        profile = Profile("1", "Test Profile", leader)
        member = User("member", "member@example.com", "password")
        profile.add_member(member)
        self.assertIn(member, profile.members)

    def test_task_update_priority(self):
        user = User("assignee", "assignee@example.com", "password")
        task = Task("Test Task", "Description", [user])
        task.update_priority(Priority.HIGH)
        self.assertEqual(task.priority, Priority.HIGH)

    def test_task_update_status(self):
        user = User("assignee", "assignee@example.com", "password")
        task = Task("Test Task", "Description", [user])
        task.update_status(Status.DOING)
        self.assertEqual(task.status, Status.DOING)

if __name__ == "__main__":
    unittest.main()
