import unittest
from models import User, Profile, Task, Priority, Status

class TestCodeManagementSystem(unittest.TestCase):

    def setUp(self):
        User.users = []
        Profile.profiles = []

