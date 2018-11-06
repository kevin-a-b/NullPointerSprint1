from memory import Memory
from Course import Course
classlist = []
class Account:

    def __init__(self, username, password, name, address, email, phonenumber, accountFlag):
        # for accountFlag: 0 is supervisor, 1 is administrator, 2 is instructor, 3 is TA
        self.username = username
        self.password = password
        self.name = name
        self.address = address
        self.email = email
        self. phonenumber = phonenumber
        self.accountFlag = accountFlag

    def createClass(self, stringList):
        classlist.append(Course(classlist.__len__(), stringList[1]))
    def deleteClass(self, stringList):
        classlist.remove(classlist[int(stringList[1])])

    def assign_instructor_class(self, instructor, id):
        classlist[id].setInstructor(instructor)

    def unassign_instructor_class(self, id):
        classlist[id].setInstructor("No Instructor")

    def assign_TA_class(self, T, id):
        classlist[id].setTA(T)

    def unassign_TA_class(self, id):
        classlist[id].setTA["No TA"]

    def printAllClasses(self, stringlist):
        for x in range(0, len(classlist)):
            print(classlist[x].printInfo())

    def create_account(self, stringList):

        # must have the right amount of arguments
        if stringList.amount() != 7:
            raise Exception("Account Creation Error: Wrong amount of information passed")
            return

        # must have the right account permissions
        if self.accountFlag != 0:
            raise Exception("Account Creation Error: You don't have permission")
            return

        # last variable in stringList should be a number between 0-3
        if stringList[7] is not int:
            raise Exception("Account Creation Error: Wrong account type")
            return

        # account flag must be 0-3
        if stringList[7]<0 or stringList>3:
            raise Exception("Account Creation Error: Invalid permissions given")
            return

        if stringList[7] is int and stringList[7]<0 or stringList[7]>3:
            raise Exception("Account Creation Error: Invalid account type")
            return

        # call constructor with correct information
        newAccount = Account(stringList[0], stringList[1], stringList[2], stringList[3], stringList[4], stringList[5], stringList[6])

        # write it to memory
        Memory.write_account(newAccount)
        return

    def delete_account(self, stringList):

        # must have the right amount of arguments
        if stringList.amount() != 1:
            raise Exception("Account Deletion Error: Wrong amount of information passed")
            return

        # must have the right account permissions
        if self.accountFlag != 0:
            raise Exception("Account Deletion Error: You don't have permission")
            return

        # username must be a str
        if stringList[0] is not str:
            raise Exception("Account Deletion Error: Incorrect username")
            return

        Memory.delete_account(stringList[0])
        return

    def edit_account_username(self, new_username):
        if self.username == new_username:
            print("it is the current username")
        elif new_username == None:
            print("plz enter something")
        else:
            self.username = new_username
            print("username updated")

    def edit_account_password(self, new_password):
        if self.password == new_password:
            print("it is the current password")
        elif new_username == None:
            print("plz enter something")
        else:
            self.password = new_password
            print("password updated")

    def edit_account_name(self, new_name):
        if self.name == new_name:
            print("it is the current name")
        elif new_username == None:
            print("plz enter something")
        else:
            self.name = new_name
            print("name updated")

    def edit_account_address(self, new_address):
        if self.address == new_address:
            print("it is the current address")
        elif new_username == None:
            print("plz enter something")
        else:
            self.address = new_address
            print("address updated")

    def edit_account_email(self, new_email):
        if self.mail == new_email:
            print("it is the current email")
        elif new_username == None:
            print("plz enter something")
        else:
            self.email = new_email
            print("email updated")

    def edit_account_phonenumber(self, new_phonenumber):
        if self.phonenumber == new_phonenumber:
            print("it is the current phonenumber")
        elif new_username == None:
            print("plz enter something")
        else:
            self.phonenumber = new_phonenumber
            print("phonenumber updated")
 
myDict = {"createaccount": "createAccount","deleteaccount": "deleteAccount", "createclass": createClass,
              "editaccount": "editaccounts(username)", "printallclass": printAllClasses, "deleteclass": deleteClass}


