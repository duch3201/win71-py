import sys
import os
import zlib
from cryptography.fernet import Fernet
import platform


def bootup():
    #bootcfg_spliced = ""
    os.chdir("..")
    os.chdir("root")
    if platform.system() == "Windows":
        with open("boot.cfg", "r") as bootcfg:
            contentsbootcfg = bootcfg.readlines()
            print(contentsbootcfg[0])
            bootcfg_spliced = contentsbootcfg[0].replace("topos =", "")
            print(bootcfg_spliced)
            #os.chdir("..")
            print(os.getcwd())


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
    bootup()
    try:
        test = os.getcwd()
        print(test)
        print("welcome to win71!", '\n', "please login")
        username = input("username: ")
        password = input("password: ")
        with open("tmpusrfile.user", "w") as tmpusrfile:
            tmpusrfile.writable()
            tmpusrfile.write(str(username))
            tmpusrfile.write("\n")
            tmpusrfile.write(password)



        #hashed_password = hash(password)

        #with open('boot.cfg', 'r', encoding='utf-8') as file:
         #   data = file.readlines()
        
        #print(data)
        #data[1] = hashed_password
        
        #with open('boot.cfg', 'w', encoding='utf-8') as file:
         #   file.writelines(str(data))

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

        #encrypt the password
        #key = Fernet.generate_key()
        #f = Fernet(key)
        #encrypted = f.encrypt(password.encode())
        #with open("tmpusrfile.user", 'w+b') as enctmp_usr_file:
         #   enctmp_usr_file.write(encrypted)
        
        #write the username to the tmp file
        #with open("tmpusrnamfile.user", 'w') as usrnam_file:
         #   usrnam_file.write(username)

        #write the key to memory for decryption
        #os.chdir("..")
        #os.chdir("boot")
        #with open("enc.key", 'wb') as key_file:
         #   key_file.write(key)


    #global setupfinised
    #setupfinised = False
    #print("Reading required files...")
    #print(os.getcwd())

    #Read the encryption key
    #os.chdir("..")
    #os.chdir("boot")
    #enckey = open("enc.key", "rb").read()
    #print(os.getcwd())
    #Read the tmpfiles
    #os.chdir("..")
    #os.chdir("tmp")
    #print(os.getcwd())
    #global usrfile
    #global username
    #usrfile = open("tmpusrfile.user", "r").read()
    #username = open("tmpusrnamfile.user", "r").read()
    #setupfinised = True
    #global F
    #F = Fernet(enckey)