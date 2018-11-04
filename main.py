from Course import Course
classlist = []

class main:


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
