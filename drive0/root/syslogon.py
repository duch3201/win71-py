import sys
import os
#import main

os.chdir("..")
os.chdir("tmp")

def login():
    try:
        test = os.getcwd()
        print(test)
        print("welcome to win71!", '\n', "please login")
        username = input("username: ")
        password = input("password: ")
        tempwrite = open("tmpusrfile", "w")
        tempwrite.write(username)
        tempwrite.write(password)
        tempwrite.close()        
        os.chdir("..")
        os.chdir("root")
        
        return username

    except KeyboardInterrupt:
        print("keybord interupt detected!")

login()






        #try:
         #   Wusrfile = open(username + ".user", "w")
         #   usrfile = open(username + ".user", "r")    
       # except FileNotFoundError:
        #    print("incorrect username or password")
         #   sys.exit()

        #usrfile = open(usrfile, "r")
        #usrfile.read()
        #print(usrfile.read())
        #test = input("press enter to continue")



        #with open(usrfile, 'r') as file:
         #   file = file.dump()
          #  search_word = input("Loggedin=TRUE") # this 
           # if search_word in usrfile:
            #    usrfile[1] = "Loggedin=FALSE"
             #   with open(usrfile, 'w', encoding='utf-8') as file:
              #      file.writelines(usrfile)
               #
                #print("an error accured and you have been logged out")
                #login()
            #else:
             #   if usrfile.read() == password:
              #      print("login successful")
               #     os.chdir("..")
                #    os.chdir("tmp")
                 #   tmpusrfile = open("rw")
                  #  tmpusrfile.write(username)
                   # tmpusrfile.close()
                    #os.chdir("..")
                    #os.system('python main.py')