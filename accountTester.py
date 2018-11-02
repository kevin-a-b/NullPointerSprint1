from account import Account
import unittest


class TestAccountMethods(unittest.TestCase):

    def setUp(self):
        self.superAccount = Account('SuperUser', 'SuperPass', 'SuperName', 'SuperAdd', 'SuperEmail', "1234567980", 0)

    def test_createAccount_wrong_list_length(self):
        with self.assertRaises(Exception):
            Account.create_account(self.superAccount, ['user', 'pass', 'name', 'address'])


if __name__ == '__main__':
    unittest.main()
