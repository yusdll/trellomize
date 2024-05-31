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

