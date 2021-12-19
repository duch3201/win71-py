import sys
import os
from cryptography.fernet import Fernet
import getpass
import platform
import subprocess
import psutil
from colorama import init, Fore, Back, Style
import shutil

def install(install_destination):
    print(Fore.GREEN + "Installing vin71 to " + install_destination)
    os.chdir("install_source")
    install_source = os.getcwd()
    mainfile = open("main.vin71", "r")
    mainfile.read()
    print(mainfile)
    syslogonfile = open("syslogon.vin71", "r")
    syslogonfile.read()
    print(syslogonfile)

    print(os.getcwd())
    try:
        os.chdir(install_destination)
    except FileNotFoundError:
        os.mkdir(install_destination)
        os.chdir(install_destination)
    print(Fore.GREEN + "Installing...")
    try:
        os.mkdir("vin71")
    except FileExistsError:
        print("there is a vin71 folder in this directory")
    os.chdir("vin71")
    os.mkdir("boot")
    os.mkdir("home")
    os.mkdir("root")
    os.mkdir("tmp")
    os.mkdir("apps")
    print(Fore.GREEN + "Copying files...")
    os.chdir("root")
    new_mainfile = open("main.py", "w")
    new_mainfile.write(mainfile)
    new_mainfile.close()
    new_syslogonfile = open("syslogon.py", "w")
    new_syslogonfile.write(syslogonfile)
    new_syslogonfile.close()
    os.chdir("..")
    print(os.getcwd())

    print(Fore.GREEN + "files copied.")

def prepforinstall():
    print(Fore.GREEN + "Welcome to the setup script for vin71.")
    print(Fore.GREEN + "This script will help you install the os.")
    print(Fore.GREEN + "Please enter install destination.")
    install_destination = input("Install destination: ")
    print(Fore.GREEN + "The install destination is: " + install_destination + "is that correct? (y/n)")
    if input() == "y" or "Y":
        install(install_destination)


prepforinstall()