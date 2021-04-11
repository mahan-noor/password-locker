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
    return user.display_user

