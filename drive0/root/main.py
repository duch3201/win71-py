import sys
import os



def shutdown():
    print("Shutting down...")
    #need to add a proper way to shutdown the system
    sys.exit()

def main(username): 
    readreqfils()

    print("Hello, " + username + "!")
    print("What would you like to do?")

    try:
        command = input("Enter command: ")
        if command == "quit":
            shutdown()
        if command == "cd":
            directory = input("Enter directory: ")
            os.cwd(directory)
            main()
        if command == "mkdir":
            directory = input("Enter directory: ")
            os.mkdir(directory)
            main()
        if command == "rmdir":
            directory = input("Enter directory: ")
            os.rmdir(directory)
            main()
        if command == "ls": #fix this so it will list files and directories
            FTP.retrlines("LIST")
            main()
        if command == "rm":
            file = input("Enter file: ") #add a warning for deleting system files
            print("are you sure you wan't to delete the file? (Y/n)")
            option = input(": ")
            if option == "Y" or option == "y":
                os.remove(file)
                print("% s has been removed successfully" % file)
                main()
            if option == "N" or option == "n":
                print("operation canceled")
                main()
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
            main()
    except KeyboardInterrupt:
        shutdown()


def readreqfils():
    print("Reading required files...")
    os.chdir("tmp")
    tmpusrfile = ""
    username = ""
    username = open( tmpusrfile, "r")
    print("done!")
    main(username)








