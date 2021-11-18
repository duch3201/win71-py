import sys

def main(): 
    command = input("Enter command: ")
    if command == "quit":
        FTP.close()
    if command == "cd":
        directory = input("Enter directory: ")
        FTP.cwd(directory)
        main()
    if command == "mkdir":
        directory = input("Enter directory: ")
        FTP.mkd(directory)
        main()
    if command == "rmdir":
        directory = input("Enter directory: ")
        FTP.rmd(directory)
        main()
    if command == "ls":
        FTP.retrlines("LIST")
        main()
    if command == "rm":
        file = input("Enter file: ")
        print("are you sure you wan't to delete the file? (Y/n)")
        option = input(": ")
        if option == "Y" or option == "y":
            FTP.delete(file)
            main()
        if option == "N" or option == "n":
            main()
    if command == "help":
        print("---------------|help|---------------")  
        print("""
        cd - change directory
        mkdir - make directory
        rmdir - remove directory
        ls - list directory
        rm - remove file
        quit - quit program
        """)
        main()


main()