import sys
import os
import syslogon
from cryptography.fernet import Fernet

username = ""
setupfinised = False 
    

def readreqfiles(setup):
    global setupfinised
    setupfinised = False
    print("Reading required files...")
    #Read the encryption key
    os.chdir("..")
    os.chdir("boot")
    enckey = open("enc.key", "rb").read()
    #Read the tmpfiles
    os.chdir("..")
    os.chdir("tmp")
    global usrfile
    global username
    usrfile = open("tmpusrfile.user", "r").read()
    username = open("tmpusrnamfile.user", "r").read()
    setupfinised = True
    global F
    F = Fernet(enckey)

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

print("Hello, " + username + "!")
print("What would you like to do?")

def main(username, usrfile, F): 
 
    try:
        while True:
            currdir = os.getcwd()
            currdir = currdir.replace("/home/duch3201/Desktop/win71-py/", "") 
            command = input(os.getcwd() + ": ")
            if command == "quit":
                shutdown()
            if command == "cd":
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
            if command == "rm":
                file = input("Enter file: ") #add a warning for deleting system files
                auth(F, usrfile)
                if usr_action_confirmed == True:
                    os.remove(file)
                    usr_action_confirmed = False
                
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
main(username, usrfile, F)


