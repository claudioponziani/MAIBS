import demo_class

class Student(demo_class.Person):
    
    def __init__(self, firstName, lastName):
        super(Student, self).__init__(firstName, lastName)
        self.gradutationYear = 2021

    def welcome(self):
        print("Welcome, {}, to the class of {}".format(self.getFullname(), self.gradutationYear))

    def getFullname(self):
        return self.firstName + " " + self.lastName

    def getFullname(self, graduationYear=2021):
        return self.firstName + " " + self.lastName + " " + graduationYear