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


















