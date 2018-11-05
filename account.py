from memory import Memory

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

