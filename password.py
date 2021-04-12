import random
import string
import pyperclip
class User:
    """
    Create class thats generates new instance of a user
    """ 
    user_list = []

    def __init__(self, username, password):

        #init method
        self.username = username
        self.password = password

    def save_user(self):

        """
        mehod that save users object into the userlist

        """
        User.user_list.append(self)

    @classmethod
    def display_user(self):
        """
        method that return the user list
        """
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method delete a saved account from the list
        '''
        User.user_list.remove(self)

class Credentials():
    '''
    create credential class to help create new objects of credential
    '''

    credentials_list = []
    @classmethod
    def verify_user(cls,username,password):
        """
        method to verify whether user is in our user_list or not
        """

        a_user = ""
        for user in user.user_list:
            if(user.username == username and user.password== password):
                    a_user == user.username

            return a_user
    def __init__(self,account,userName,password):
        """
        method that define users credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password

    
    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists or if it does not.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.credentials_list

    def generatePassword(stringLength=7):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^"
        return ''.join(random.choice(password) for i in range(stringLength))

                
             







        








        