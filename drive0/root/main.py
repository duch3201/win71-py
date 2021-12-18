import sys
import os
import syslogon
from cryptography.fernet import Fernet
import getpass
import platform


global setupfinised
username = ""
password = ""
usr_action_confirmed = False
setupfinised = False 
host_os = "Windows"
top_dir = ""
currdir = ""
irlusrname = getpass.getuser()


def readreqfiles(setupfinised):
    global username
    host_os = ""
    global currdir
    #get the top directory
    os.chdir("..")
    os.chdir("..")
    top_dir = os.getcwd()
    print(top_dir)
    os.chdir("drive0")
    setupfinised = False
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

def auth(password, usr_action_confirmed):
    passconfirm = input("Enter password: ")
    if passconfirm == password:
        usr_action_confirmed = True
    else:
        print("Incorrect password")
        usr_action_confirmed = False



    # #this function will be used to confirm the users choice?
    # print("Enter your password")
    # passconf = input(": ")
    # epassconf = F.encrypt(passconf.encode())
    # if epassconf == usrfile:
    #     usr_action_confirmed = True
    #     return
    # else:
    #     usr_action_confirmed = False
    #     print("incorrect password")
    #     return

    

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

def main(username, host_os, currdir, top_dir): 
    global usr_action_confirmed
    try:
        while True:
            #this code replaces the standard path in the command input
            if host_os == "Linux":
                currdir = os.getcwd()
                currdir = currdir.replace("/home", "")
                currdir = currdir.replace("/Desktop/win71-py/", "") 
                currdir = currdir.replace(irlusrname, "")
            if host_os == "Windows":
                currdir = os.getcwd()
                currdir = currdir.replace("D:\\package man", "")
                currdir = currdir.replace("/drive0/", "")
                #currdir = currdir.replace(irlusrname, "")

            print(top_dir)
            print(platform.system())
            print(host_os)
            command = input(currdir + ": ")

            if command == "quit":
                shutdown()
            if command.startswith("cd"):
                os.chdir(command.replace("cd ", ""))
            if command.startswith("mkdir"):
                os.mkdir(command.replace("mkdir", ""))
            if command.startswith("rmdir"):
                os.rmdir(command.replace("rmdir ", ""))
            if command == "ls": #fix this so it will list files and directories
                print(os.listdir())
            if command == "osinfo":
                #if command == "osinfo -i":
                print(platform.system() + " " + platform.release())
            if command == "rm":
                file = input("Enter file: ") #add a warning for deleting system files
                auth(password, usr_action_confirmed)
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
main(username, host_os, currdir, top_dir)


