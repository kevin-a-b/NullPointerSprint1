
class Course:
    def __init__(self,cCode, cName):
        self.classCode = cCode
        self.className = cName
    def setClassCode(self, id):
        self.classCode = id
    def setClassName(self,name):
        self.className = name
    def setInstructor(self,instruct):
        self.instructor = instruct
    def setTA(self, T):
        self.TA = T
    def getClassCode(self):
        return(self.classCode)
    def getClassName(self):
        return(self.className)
    def getInstructor(self):
        return(self.instructor)
    def getTA(self):
        return(self.TA)