import unittest
from  password import User
from  password import Credentials

class TestClass(unittest.TestClass):

    '''
    Test class that defines test case for the user class

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("IsmahanAbey", "BxF6th2")

    def test_init(self):
        """
        test_init to check if the object is initialization properly
        """
        self.assertEqual(self.new_user.username,"IsmahanAbey")
        self.assertEqual(self.new_user.password,"BxF6th2")


