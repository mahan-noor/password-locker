#!/usr/bin/env python3.8
from password import User, Credentials

def create_new_user(username,password):
    '''
    Function to create a new user with username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    function to save new user
    '''
    user.save_user()

def display_user():
    """
    Function to display the existing user
    """
    return user.display_user()

def login_user(username,password):
    """
    function that checks and login the user
    """
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    """
    Fuction to create new credentials for user given account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential

def save_credential(credentials):
    """
    Function to save users credential to the credential list
    """
    credentials.save_details()

def display_accounts_details():
    """
    a function that returns all saved credentials
    """
    return Credentials.display_credentials()

def delete_credential(account):
    """
    function that delete credentials from credential list
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    function that find the user credential by the account name and returns true or false
    """
    return Credentials.find_credential(account)

def check_credentials(account):
    """
    Function that checks if the credential exist
    """
    return Credentials.if_credential_exist(account)

def generate_password():
    """
    generate a random password for the user
    """
    auto_password= Credentials.generate_password()
    return auto_password

def copy_password(account):
    """
    a function that copies password using pyperclip
    we import pyperclip then declare a fuction that copies
    """
    return Credentials.copy_password(account)   

def password():
    print("Hello welcome to you account pass lock...\n Please enter one of the following to proceed.\n CA --- Create New Account  \n LI --- Have An Account  \n")
    short_code =input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 45)
        username =input("user_name")
        while True:
            print("TP- type your own password:\n GP-generate a random password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter your password")
                break
            elif password_Choice == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*" *83)
        print(f"Hey {username}, Your account has been created succesfully. Your password is {password}")
        print("*"*83)
    elif short_code == "li":
        print("*"*50)
        print("Enter your username and password to login")
        print("*"*50)
        username = input("username: ")
        password = input("password: ")
        if login_user = login:
            print(f"Hello{username}.Welcome to password-locker manager")
            print('\n')
        



















