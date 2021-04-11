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


class TestCredentials(unittest.TestCase):
    """
    A test class that define test case for credentials class
    """
    def setUp(self):
        """
        setup up test to run before each test
        """
        self.new.credential = Credentials('Instagram','Ismahan_noor', 'yhi6ug0')
    
    def test_init(self):
        """
        Test case to see if the object is initialized properly
        """
        self.assertEqual(self.new_credential.account,'Instagram')
        self.assertEqual(self.new_credential.username,'Ismahan_noor')
        self.assertEqual(self.new_credential.password,'yhi6ug0')

    def save_credential_test(self):
        """
        Test case to test if credential object is saved in credential list
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        """
        Test case that does clean up after each test has run
        """
        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        """
        Test case to check if  we have multiple credential objects in our credential list
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","mahan-noor","Cfhu56g")
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list)2)

    def test_delete(self):
        """
        Test to check if we can delete account credential

        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","mahan-noor","Cfhu56g")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list)1)

    def test_find_credentials(self):
        """
        test to check if we can find credential of the account name and display details of the credentials
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","mahan-noor","Cfhu56g")
        test_credential.save_details()

        the_credential = Credentials.test_find_credentials("Twitter")

        self.assertEqual(the_credential.account,test_credential.account)

    
    def test_credential_exist(self):
        """
        Test to see return a true and false based on whether we can find or not find credential
        """
        self.new_credential.save_details()
        the_credential =Credentials("Twitter","mahan-noor","Cfhu56g")
        the_credential.save_details()
        creditial_is_found = Credentials.if_credential_exist("Twitter")
        self.assertTrue(creditial_is_found)

    def test_display_all_saved_credentials(self):
        '''
        method that shows all the credential saved by the user
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()


