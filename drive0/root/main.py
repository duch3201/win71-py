import sys
import os
import syslogon
from cryptography.fernet import Fernet
import getpass
import platform

global username
global setupfinised
username = ""
password = ""
setupfinised = False 
irlusrname = getpass.getuser()


def readreqfiles(setupfinised):
    setupfinised = False
    os.chdir("..")
    os.chdir("root")
    if platform.system() == "Windows":
        host_os = "Windows"
    if platform.system() == "Linux":
        host_os = "Linux"
    if platform.system() == "Darwin":
        host_os = "Mac"
    with open("tmpusrfile.user", 'r') as tmpusrfile:
        content = tmpusrfile.readlines()
        username = content[0]
        password = content[1]
        print(content[0])
        print(content[1])
        print(username)
        print(password)

def auth(F, usrfile):
    #this function will be used to confirm the users choice?
    print("Enter your password")
    passconf = input(": ")
    epassconf = F.encrypt(passconf.encode())
    if epassconf == usrfile:
        usr_action_confirmed = True
        return
    else:
        usr_action_confirmed = False
        print("incorrect password")
        return

    

def shutdown():
    print("Shutting down...")
    os.chdir("..")
    os.chdir("boot")
    os.remove("enc.key")
    os.chdir("..")
    os.chdir("tmp")
    os.remove("tmpusrfile.user")
    sys.exit()

print("What would you like to do?")

def main(username): 
    
    try:
        while True:
            #this code replaces the standard path in the command input
            currdir = os.getcwd()
            currdir = currdir.replace("/home", "")
            currdir = currdir.replace("/Desktop/win71-py/", "") 
            currdir = currdir.replace(irlusrname, "")
            
            command = input(currdir + ": ")

            if command == "quit":
                shutdown()
            if command == "cd":
                #command = input("Enter the directory you would like to go to: ")
                print(command)
                command = command.replace("cd", "")
                os.chdir(command)
                print(command)
                #directory = input("Enter directory: ")
                #print(directory)
                #os.chdir(directory)
            if command == "mkdir":
                directory = input("Enter directory: ")
                os.mkdir(directory)
            if command == "rmdir":
                directory = input("Enter directory: ")
                os.rmdir(directory)
            if command == "ls": #fix this so it will list files and directories
                print(os.listdir())
            if command == "osinfo":
                #if command == "osinfo -i":
                print(platform.system() + " " + platform.release())
            if command == "rm":
                file = input("Enter file: ") #add a warning for deleting system files
                auth()
                if usr_action_confirmed == True:
                    os.remove(file)
                    usr_action_confirmed = False
            if command == "whoami":
                print(username)
            if command == "watmypass":
                print(password)
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
    except KeyboardInterrupt:
        shutdown()




if setupfinised == False:
    readreqfiles(setupfinised)
main(username)


