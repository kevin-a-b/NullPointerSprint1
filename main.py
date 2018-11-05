from Course import Course
from memory import Memory

classlist = []

cmd = {}
# Command list for main class


def set_user(user):  # Set current user
    global current_user # set global so it can be accessed from other methods in this file
    current_user = user


def getuser():  # Get current user(for external files) PEP8 makes
    return current_user


class Project:
    def __init__(self):
        self.commands = cmd

    def command(self, strcmd):
        split = strcmd.split()
        return self.commands[split[0]](split[1:])

    def createClass(self,cName):
        classlist.append(Course(classlist.__len__(), cName))
    
    def assign_instructor_class(self, instructor,id):
        classlist[id].setInstructor(instructor)
    
    def unassign_instructor_class(self,id):
        classlist[id].setInstructor("No Instructor")
    
    def assign_TA_class(self,T,id):
        classlist[id].setTA(T)
    
    def unassign_TA_class(self, id):
        classlist[id].setTA["No TA"]
    
    def printAllClasses(self):
        for x in range(0,len(classlist)):
            print(classlist[x].printInfo())


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
