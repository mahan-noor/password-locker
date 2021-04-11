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

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved in the user list
        '''
        self.new_user.save_user() #saving new user
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()


