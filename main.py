from Course import Course
from memory import Memory
from account import Account

x = 2
cmd = {}
# Command list for main class
#genericaccount
a = Account("","username","password","address","Email","Phone",3)

def set_user(user):  # Set current user
    global current_user  # set global so it can be accessed from other methods in this file
    current_user = user
    

def getuser():  # Get current user
    return current_user


class Project:
    def __init__(self):
        set_user(None)
        self.commands = cmd
    #displays all commands available to the user
    def help(self):
        print("createaccount <username> <password> \n"
              "deleteaccount <username> \n"
              "createclass <classname>\n"
              "printallclass \n"
              "deleteclass <classid#> \n"
              "addta <taname> <classid#>\n"
              "removeta <classid#>\n"
              "addinstructor <instructor name> <classid#>\n"
              "removeinstructor <classid#>\n")

    #loop for command line interface
    set_user(a)
    inCommand = "start"
    while inCommand[0] != "exit":
        i = input("Please Input a Command,type 'help' for a list of commands\n")
        inCommand = i.split(" ")
        if inCommand[0] == "exit":
            break
        elif inCommand[0] =="help":
            help("")
        else:
            try:
                getuser().myDict[inCommand[0]](current_user,inCommand)
            except:
                print("error has occurred, type in a recognized command")


def login(user_pass):  # user_pass short for list contained username and password
    user = current_user  # For some reason we can't directly use current_user but we can set stuff to it
    if len(user_pass) != 2:  # If wrong amount of arguments
        return "Error"
    elif not (user is None):  # If a user is logged in already logged in
        return "Another User is logged in"
    else:
        user = Memory.read_account(user_pass[0], user_pass[1])
        if user is None:
            return "Error"
        set_user(user)
        return "Login Success"


cmd["login"] = login  # Add login command to command list


def logout(extra):  # Log Off Command, extra is unnecessary arguments passed through
    if len(extra) > 0:  # If any extra arguments
        return "Error"
    user = current_user
    if user is None:  # We can't logoff if there is nobody to logoff
        return "Error"
    else:  # Set current user to none since no one is logged in
        set_user(None)
        return "Logout Success"


cmd["logout"] = logout  # Add logoff command to command list
