import sys
import os
import syslogon
import exec
import getpass
import platform
import subprocess
import psutil
from colorama import init, Fore, Back, Style


init(autoreset=True) #initialize colorama

global setupfinised
username = ""
password = ""
usr_action_confirmed = False
setupfinised = False 
host_os = "Linux"
top_dir = ""
currdir = ""
irlusrname = getpass.getuser()
Guest_OS = "vin71"
Guest_OS_build = "12.24.1"

#additional functions

def clear():
    if host_os == "Linux":
        os.system("clear")
    if host_os == "Windows":
        os.system("cls")


def update(): #for now this will just exit the program
    sys.exit()


def readreqfiles(setupfinised):
    global username
    global host_os
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
        print(Fore.RED + "Incorrect password")
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

clear()
print(Style.BRIGHT + Back.YELLOW + Fore.RED + "CHEESY")
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

            command = input(currdir + ": ")

            if command == "quit":
                shutdown()
            if command.startswith("cd"):
                try:
                    os.chdir(command.replace("cd ", ""))
                except FileNotFoundError:
                    print(Fore.RED + "Directory not found!")
            if command.startswith("mkdir"):
                os.mkdir(command.replace("mkdir", ""))
            if command.startswith("rmdir"):
                auth(password, usr_action_confirmed)
                if usr_action_confirmed == True:
                    try:
                        os.rmdir(command.replace("rmdir ", ""))
                    except FileNotFoundError:
                        print(Fore.RED + "Directory not found!")
                    usr_action_confirmed = False
            if command == "ls": #fix this so it will list files and directories
                print(os.listdir())
            if command == "sysinfo":
                print("System info:")
                print(Fore.GREEN + "Host OS: " + platform.system() + " " + platform.release())
                print(Fore.GREEN + "Guest OS: " + Guest_OS + " " + Guest_OS_build)
                print("cpu usage: " + str(psutil.cpu_percent()) + "%")
                print("ram usage: " + str(psutil.virtual_memory()[2]) + "%")
                print("disk usage: " + str(psutil.disk_usage("/")[3]) + "%")

            if command.startswith("rm"):
                #file = input("Enter file: ") #add a warning for deleting system files
                auth(password, usr_action_confirmed)
                if usr_action_confirmed == True:
                    try:
                        os.remove(command.replace("rm ", ""))
                    except FileNotFoundError:
                        print("File not found!")
                    usr_action_confirmed = False
            if command == "whoami":
                print(username)
            if command == "watmypass":
                print(password)
            if command.startswith("note"):
                olddir = os.getcwd()
                os.chdir("..")
                os.chdir("apps")
                if host_os == "Linux" or host_os == "Darwin":
                    os.chdir("notepad for linux")
                    exec(open("notepA.py").read())
                    #os.chdir(olddir)
                if host_os == "Windows":
                    os.chdir("my-notepad")
                    exec(open("Notepad.py").read())
                    #os.chdir(olddir)
            if command.startswith("calc"):
                olddir = os.getcwd()
                os.chdir("..")
                os.chdir("apps")
                os.chdir("calculator")
                #os.system("Calculadora.exe")
                #exec(open("main.py").read())
                
                #os.chdir(olddir)
                
            if command == "help":
                print("---------------|help|---------------")  
                print("""
                cd - change directory
                mkdir - make directory
                rmdir - remove directory
                ls - list directory
                rm - remove file
                whoami - show username
                sysinfo - show system information
                quit - shutdown the system
                note - open notepad
                calc - open calculator
                help - show this menu
                """)
    except KeyboardInterrupt:
        shutdown()




if setupfinised == False:
    readreqfiles(setupfinised)
main(username, host_os, currdir, top_dir)

