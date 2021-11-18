import sys
import os

os.chdir("..")
os.chdir("home")

print("welcome to win71!", '\n', "please login")
username = input("username: ")
password = input("password: ")

try:
    usrfile = open(username + ".user", "rw")
except FileNotFoundError:
    print("incorrect username or password")
    sys.exit()