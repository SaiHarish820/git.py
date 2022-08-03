class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)


x = Person("CSE","PFSD")
x.printname()

# Program 2

class Parent:
    # Constructor
    def __init__(self, txt):
        self.message = txt

    # To check if this person is an Parent
    def printmessage(self):
        print(self.message)

class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)

x = Child("Hello!") # An Object of Child

x.printmessage()

# Random Function Program

import random
n = random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,200))
mylist = ["Jadeja", "Ashwin",]
