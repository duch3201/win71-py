import os
import sys
import getpass
import platform


def ofb():
    print("please enter your username")
    username = input(": ")
    print("please enter your password")
    password = getpass.getpass(": ")
    print("please enter your password again")
    password2 = getpass.getpass(": ")
    if password == password2:
        print("password confirmed")
        os.chdir("..")
        os.chdir("drive0")
        os.chdir("home")
        with open("usr.user", "w+b") as usrfile:
            usrfile.write(hash(password))
            
    else:
        print("passwords do not match")
        ofb()


ofb()