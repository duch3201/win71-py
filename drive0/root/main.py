import sys
import os
import syslogon
from cryptography.fernet import Fernet

username = ""
setupfinised = False
currdir = os.getcwd()  
currdir = currdir.replace("/home/duch3201/Desktop/win71-py/", "")     

def readreqfiles(setup):
    setupfinised = False
    print("Reading required files...")
    #Read the encryption key
    os.chdir("..")
    os.chdir("boot")
    enckey = open("enc.key", "rb").read()
    #Read the tmpfiles
    os.chdir("..")
    os.chdir("tmp")
    usrfile = open("tmpusrfile.user", "r").read()
    username = open("tmpusrnamfile.user", "r").read()
    setupfinised = True

    

    

def shutdown():
    print("Shutting down...")
    os.chdir("..")
    os.chdir("boot")
    os.remove("enc.key")
    os.chdir("..")
    os.chdir("tmp")
    os.remove("tmpusrfile.user")
    sys.exit()

print("Hello, " + username + "!")
print("What would you like to do?")

def main(username): 


    try:
        command = input(currdir + ": ")
        if command == "quit":
            shutdown()
        if command == "cd":
            directory = input("Enter directory: ")
            print(directory)
            os.chdir(directory)
            main(username)
        if command == "mkdir":
            directory = input("Enter directory: ")
            os.mkdir(directory)
            main(username)
        if command == "rmdir":
            directory = input("Enter directory: ")
            os.rmdir(directory)
            main(username)
        if command == "ls": #fix this so it will list files and directories
            os.listdir()
            main(username)
        if command == "rm":
            file = input("Enter file: ") #add a warning for deleting system files
            print("are you sure you wan't to delete the file? (Y/n)")
            option = input(": ")
        if option == "Y" or option == "y":
            os.remove(file)
            print("% s has been removed successfully" % file)
            main(username)
        if option == "N" or option == "n":
            print("operation canceled")
            main(username)
        if command == "help":
            print("---------------|help|---------------")  
            print("""
            cd - change directory
            mkdir - make directory
            rmdir - remove directory
            ls - list directory
            rm - remove file
            quit - shutdown the system
            """)
            main(username)
    except KeyboardInterrupt:
        shutdown()




if setupfinised == False:
    readreqfiles(setupfinised)
else:
    main(username)









