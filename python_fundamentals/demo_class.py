class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFullname(self):
        return self.lastName + " " + self.firstName
