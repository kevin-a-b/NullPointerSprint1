from main import Project
import unittest

console = Project()


class TestCases(unittest.TestCase):
    def test_login(self):
        self.assertEqual(console.command("login <User> <Password>"), "Log in Success")  # Assume no users logged in

    def test_logoff(self):
        self.assertEqual(console.command("logout"), "Log out Success")  # Assume any user logged in

    def test_createCourse(self):
        self.assertEqual(console.command("createclass <Course>"), "Course Created")  # Assume supervisor logged in

    def test_createAccount(self):
        self.assertEqual(console.command("createaccount <NewUser> <NewPassword>"), "Account Created")  # Assume supervisor logged in

    def test_deleteAccount(self):
        self.assertEqual(console.command("deleteaccount <User>"), "Account Deleted")  # Assume supervisor logged in with at least 1 user account

    def test_editAccount(self):
        self.assertEqual(console.command("editaccount <User>"), "Account Changed")  # Assume supervisor logged in with at least 1 user account

    def test_sendNotice(self):
        self.assertEqual(console.command("sendnotice <User> <Message>"), "Notice Sent")  # Assume Supervisor logged in with at least 1 user account

    def test_accessDataAll(self):
        self.assertEqual(console.command("accessalldata <User>"), "User Address Email Number")  # Assume Supervisor logged in with at least 1 user account

    def test_assignInstructor(self):
        self.assertEqual(console.command("assigninstructorclass <Instructor> <Class>"), "Instructor Assigned")  # Assume Supervisor logged in with at least 1 instructor account and 1 course

    def test_assignTACourse(self):
        self.assertEqual(console.command("assigntaclass <TA> <Class>"), "TA Assigned")  # Assume Supervisor logged in with at least 1 TA account, 1 instructor account, and 1 course

    def test_assignTALab(self):
        self.assertEqual(console.command("assigntalab <TA> <Lab>"), "TA Assigned")  # Assume Supervisor logged in with at least 1 TA account, 1 instructor account, and 1 course

    def test_instructorEditAccount(self):
        self.assertEqual(console.command("changecontactinfo <username>"), "Info Edited")  # Assume instructor logged in

    def test_taChangeContactNumber(self):
        self.assertEqual(console.command("editcontactnumber <username>"), "Number Edited")  # Assume TA logged in

    def test_taViewAssignments(self):
        self.assertEqual(console.command("viewmylabs"), "Assignment is Lab 0")  # Assume Ta logged in and is assigned to labs

    def test_checkTA(self):
        self.assertEqual(console.command("viewmyta"), "TA1\nTA2") # Assume instructor is logged in and assigned to course that also has multiple TA's assigned

    def test_viewContact(self):
        self.assertEqual(console.command("viewcontactinfo <User>"), "User Email")  # Assume any user logged in with at least 1 other user account

    def test_emailTA(self):
        self.assertEqual(console.command("sendnotice <TA>"), "Notice Sent")  # Assume instructor logged in with assigned TA to course

    def test_instructorAssignTA(self):
        self.assertEqual(console.command("assigntalab <TA> <Lab>"), "TA Assigned")  # Assume instructor logged in with TA assigned to course and lab assigned to course

    def test_instructorAccessInfo(self):
        self.assertEqual(console.command("viewcontactinfo <User>"), "User Number")  # Assume instructor logged in with at least one other user account


if __name__ == '__main__':
    unittest.main()