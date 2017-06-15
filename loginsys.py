###To be added:################################################
#1-Mysql system                                                #
#2-Chat system                                                 #
#3-GUI   													   #
#4-Encryption                                                  #                      								   #
################################################################








import os
import getpass
#import base64
import string
import time
#from tkinter import * ##soon
#import chat ##soon
#import chatserver ##soon
os.system('cls' if os.name=="nt" else 'clear')
class bcolors:
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'

version = bcolors.OKBLUE + "8.0 Alpha" + bcolors.ENDC



#def encryption():
    #Working on it.


def changepass():

    username = input("Please enter your username: ")
    if os.path.isfile(username + ".txt") == False:
        print("Wrong username. Try again.")

        changepass()
    else:
        with open(username + ".txt", "r") as f:
            password = getpass.getpass("Enter old password: ")
            if not password:
                print("Try again.")
                f.close()
                changepass()
            if password == f.read():
                print("Passwords match. Now you can change password. Select new password to yourself.")
                f.close()
                changed = getpass.getpass(">>> ")
                if not changed:
                    print("You can not leave password empty")
                    time.sleep(1)
                    os.system('cls' if os.name == "nt" else 'clear')
                    loggedin()
                else:
                    with open(username + ".txt", "w") as s:
                        s.truncate()
                        s.write(changed)
                        s.close()
                        print("Pass change succesful! Redirecting to your account.")
                        s.close()
                        time.sleep(1)
                        os.system('cls' if os.name == "nt" else 'clear')
                        loggedin()
            else:
                print(bcolors.FAIL + "Your password doesnt match." + bcolors.ENDC)
                loggedin()

def loggedin():
    whattodo = input("Options is:\n1.Chat\n2.Change password\n3.Switch account\n4.Exit\n")
    if whattodo == "1":
        print("\ncoming soon\n")
        time.sleep(2)
        loggedin()
    elif whattodo == "2":
        changepass()
    elif whattodo == "3":
        print("Goodbye!")
        login()
    elif whattodo == "4":
        print("Goodbye!")
        exit()
    else:
        print("Wrong button!")
        loggedin()


def comingsoon():
    print("----------------------------------------")
    print("|            Coming Soon               |")
    print("----------------------------------------")


def login():
    print (bcolors.OKGREEN + "----------------------------------------")
    print ("|                Login                 |")
    print ("----------------------------------------" + bcolors.ENDC)
    k_name = input(bcolors.OKGREEN + "Enter username: " + bcolors.ENDC)
    if os.path.exists(k_name + ".txt") == False:
        print (bcolors.FAIL + "Username not found." + bcolors.ENDC)
        create()
    else:
        k_pass = getpass.getpass(bcolors.OKGREEN + "Enter password: " + bcolors.ENDC)
        with open(k_name + ".txt", "r") as f:
            if k_pass == f.read():
                print(bcolors.OKBLUE + "\nWelcome ", k_name + bcolors.ENDC)
                f.close()
                loggedin()
            else:
                print(bcolors.FAIL + "Password is wrong " + bcolors.ENDC)
                create()



def create():
    print("You using login system %s" % version)
    print(bcolors.WARNING + "Alpha version (bugs not fixed && features not added)" + bcolors.ENDC)
    print(bcolors.OKGREEN + "----------------------------------------")
    print("|                 Lobby                |")
    print( "----------------------------------------" + bcolors.ENDC)
    starting = input(bcolors.OKGREEN + "To create user type R, to login type L: " + bcolors.ENDC).upper()
    if starting == "R":
        name = input("Enter username: ")
        if len(name) > 16:
            print("\rUsername cannot be longer than 16 characters!")
            time.sleep(2)
            os.system('cls' if os.name=="nt" else 'clear')
            create()
        else:
            if os.path.isfile(name + ".txt") == True:
                print(bcolors.FAIL + "Username already taken, please try another one." + bcolors.ENDC)
                name = None
                create()
            else:
                password = getpass.getpass("Enter password: ")
                if not password:
                    print("You can not leave password empty!")
                    time.sleep(1)
                    os.system('cls' if os.name == "nt" else 'clear')
                    create()
                else:
                    password2 = getpass.getpass("Verify: ")
            if password == password2:
                newfile = open(name + ".txt", "a")
                newfile.write(password)
                newfile.close()
                print(bcolors.OKBLUE + "User created. Redirecting you to login." + bcolors.ENDC)
                time.sleep(2)
                os.system('cls' if os.name == "nt" else 'clear')
                login()
            elif password != password2:
                print(bcolors.FAIL + "Passwords doesn't match." + bcolors.ENDC)
                input("Press enter to continue")
                create()

    elif starting == "L":
        login()
    elif starting == "NEW":
        comingsoon()
    else:
        print(bcolors.FAIL + "\nWrong button\n" + bcolors.ENDC)
        create()

create()