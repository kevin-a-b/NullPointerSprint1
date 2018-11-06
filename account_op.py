# In the interface draft the question that if <user_name>
# have to be using as the 2nd parameter was issued. I was
# writing considering that the user has already been login
# their own account to make following operations so the
# <user_name> parameter was not considered.

from account import Account


class account_op:

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
