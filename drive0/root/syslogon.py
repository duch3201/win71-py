import sys
import os
import zlib
from cryptography.fernet import Fernet


def generatekey():

    #this function generates a encryption key that shall be used 
    #to encrypt and decrypt the password and other strings that
    #may contain sensitive information. that we do not want to store
    #in plain text. in the near future we may use this key to encrypt
    #and decrypt user files as well as other things that we may need to
    #encrypt.
    #:)

    os.chdir("..")
    os.chdir("boot")

    key = Fernet.generate_key()

    with open("enc.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    #this function loads the encryption key
    os.chdir("..")
    os.chdir("boot")
    return open("enc.key", "rb").read()

os.chdir("..")
os.chdir("tmp")



def login():
    try:
        test = os.getcwd()
        print(test)
        print("welcome to win71!", '\n', "please login")
        username = input("username: ")
        password = input("password: ")
        tempwrite = open("tmpusrfile.user", "w")

        #encrypt the password
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted = f.encrypt(password.encode())
        with open("tmpusrfile.user", 'w+b') as enctmp_usr_file:
            enctmp_usr_file.write(encrypted)
        
        #write the username to the tmp file
        with open("tmpusrnamfile.user", 'w') as usrnam_file:
            usrnam_file.write(username)

        #write the key to memory for decryption
        os.chdir("..")
        os.chdir("boot")
        with open("enc.key", 'wb') as key_file:
            key_file.write(key)

    except KeyboardInterrupt:
        print("keybord interupt detected!")

login()



        #might need this code below later


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