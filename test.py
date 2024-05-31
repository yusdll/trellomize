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
        
        