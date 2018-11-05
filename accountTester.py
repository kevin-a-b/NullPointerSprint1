from account import Account
import unittest


class TestAccountMethods(unittest.TestCase):

    def setUp(self):
        self.superAccount = Account('SuperUser', 'SuperPass', 'SuperName', 'SuperAdd', 'SuperEmail', "1234567980", 0)
        self.TAAccount  = Account('TAUser', 'TAPass', 'TAName', 'TAAdd', 'TAEmail', '1234567890', 3)

    def test_createAccount_short_list_length(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address'])

    def test_createAccount_long_list_length(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', 0, 'un-needed string'])

    def test_createAccount_wrong_permissions(self):
        with self.assertRaises(Exception):
            Account.create_account(self.TAAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', 0])

    def test_createAccount_wrong_permissions_passed(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', 'not an int'])

    def test_createAccount_permission_passed_too_low(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', -1])

    def test_createAccount_permission_passed_too_high(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address', 'email', '2134235', 4])

    def test_deleteAccount_wrong_permissions(self):
        with self.assertRaises(Exception):
            Account.delete_account(self.TAAccount, ['username'])

    def test_deleteAccount_incorrect_username(self):
        with self.assertRaises(Exception):
            Account.delete_account(self.superAccount, [9])

    def test_deleteAccount_short_list(self):
        with self.assertRaises(Exception):
            Account.delete_account(self.superAccount, [])

    def test_deleteAccount_long_list(self):
        with self.assertRaises(Exception):
            Account.delete_account(self.superAccount, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
