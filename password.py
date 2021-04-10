import pyperclip
class user:
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






        