import sys
import os
import syslogon


username = ""
setupfinised = True


def shutdown():
    print("Shutting down...")
    #need to add a proper way to shutdown the system
    sys.exit()

print("Hello, " + username + "!")
print("What would you like to do?")

def main(username, setupfinised): 
    
    print("Reading required files...")
    os.chdir("..")
    os.chdir("tmp")
    username = open("tmpusrfile.user", "r") 
    username.read()
    print(username)
    os.chdir("..")
    os.chdir("home")
    os.chdir(username)   
    print("done!")

    if setupfinised == False:
        print("lol")

    else:

        try:
            command = input("Enter command: ")
            if command == "quit":
                shutdown()
            if command == "cd":
                directory = input("Enter directory: ")
                os.chdir(directory)
                main(username, setupfinised)
            if command == "mkdir":
                directory = input("Enter directory: ")
                os.mkdir(directory, setupfinised)
                main(username, setupfinised)
            if command == "rmdir":
                directory = input("Enter directory: ")
                os.rmdir(directory)
                main(username, setupfinised)
            #if command == "ls": #fix this so it will list files and directories
             #   FTP.retrlines("LIST")
              #  main(username, setupfinised)
            if command == "rm":
                file = input("Enter file: ") #add a warning for deleting system files
                print("are you sure you wan't to delete the file? (Y/n)")
                option = input(": ")
                if option == "Y" or option == "y":
                    os.remove(file)
                    print("% s has been removed successfully" % file)
                    main(username, setupfinised)
                if option == "N" or option == "n":
                    print("operation canceled")
                    main(username, setupfinised)
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
                main(username, setupfinised)
        except KeyboardInterrupt:
            shutdown()





main(username, setupfinised)





#def readreqfils(setupfinised):
 #   setupfinised = "False"
  #  os.getcwd()
   # print("Reading required files...")
    #os.chdir("..")
    #os.chdir("tmp")
    #tmpusrfile = ""
    #username = ""
    ##username = open( tmpusrfile, "r")
    #print("done!")
    #setupfinised = "True"
    #main(username)



