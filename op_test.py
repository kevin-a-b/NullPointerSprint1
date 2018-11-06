from account_op import account_op
import unittest

user = Account('Snowman', '20181225', 'SnowJackal', 'backyard',
               'merryXmas@winter.com', 414000111, 3)  # does flag number matters here?


class TestAccountMethods(unittest.TestCase):
    def test_username1(self):
        self.assertEqual(user.edit_account_username("Snowman"), "it is the current username")

    def test_username2(self):
        self.assertEqual(user.edit_account_username("Fireman"), "username updated")

    def test_username3(self):
        self.assertEqual(user.edit_account_username(), "plz enter something")

    def test_password1(self):
        self.assertEqual(user.edit_account_password("20181225"), "it is the current password")

    def test_password2(self):
        self.assertEqual(user.edit_account_password("20181231"), "password updated")

    def test_password3(self):
        self.assertEqual(user.edit_account_password(), "plz enter something")

    def test_name1(self):
        self.assertEqual(user.edit_account_name("SnowJackal"), "it is the current name")

    def test_name2(self):
        self.assertEqual(user.edit_account_name("FireFly"), "name updated")

    def test_name3(self):
        self.assertEqual(user.edit_account_name(), "plz enter something")

    def test_address1(self):
        self.assertEqual(user.edit_account_address("backyard"), "it is the current address")

    def test_address2(self):
        self.assertEqual(user.edit_account_address("street"), "address updated")

    def test_address3(self):
        self.assertEqual(user.edit_account_address(), "plz enter something")

    def test_email1(self):
        self.assertEqual(user.edit_account_email("merryXmas@winter.com"), "it is the current email")

    def test_email2(self):
        self.assertEqual(user.edit_account_email("seeyounextyear@spring.com"), "email updated")

    def test_email3(self):
        self.assertEqual(user.edit_account_email(), "plz enter something")

    def test_phonenumber1(self):
        self.assertEqual(user.edit_account_phonenumber(414000111), "it is the current phonenumber")

    def test_phonenumber2(self):
        self.assertEqual(user.edit_account_phonenumber(414222333), "phonenumber updated")

    def test_phonenumber3(self):
        self.assertEqual(user.edit_account_phonenumber(), "plz enter something")


if __name__ == '__main__':
    unittest.main()