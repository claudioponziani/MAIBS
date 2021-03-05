from demo_subclass import Student

student1 = Student('John', 'Pearson')
print(student1.gradutationYear)

try:
    student1.welcome()
except:
    print('There is an error')
    pass