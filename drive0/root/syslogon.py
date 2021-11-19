import sys
import os
import main

os.chdir("..")
os.chdir("home")

def login():
    try:
        print("welcome to win71!", '\n', "please login")
        username = input("username: ")
        password = input("password: ")

        try:
            usrfile = open(username + ".user", "r")
            usrfile = open(username + ".user", "w")
        except FileNotFoundError:
            print("incorrect username or password")
            sys.exit()

        with open(usrfile) as file:
            contents = file.read()
            search_word = input("Loggedin=TRUE") # this 
            if search_word in contents:
                usrfile[1] = "Loggedin=FALSE"
                with open('example.txt', 'w', encoding='utf-8') as file:
                    file.writelines(usrfile)

                print("an error accured and you have been logged out")
                login()
            else:
                if usrfile.read() == password:
                    print("login successful")
                    os.chdir("..")
                    os.chdir("tmp")
                    tmpusrfile = open("rw")
                    tmpusrfile.write(username)
                    tmpusrfile.close()
                    os.chdir("..")
                    main.main()


    except KeyboardInterrupt:
        print("keybord interupt detected!")

login()