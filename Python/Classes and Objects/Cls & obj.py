# What is the use of a class ?
"""A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword."""

# Creating the class 

""" syntax : class Class_name:
                Body of class
"""
# Creating an Object:

"""Object is the instance of the class used to access the properties of the class Now lets create an object of the class.

Syntax :
    obj_name = class_name()

And now we can use the object to acess the values and functions of the class. To access the memebers of class we use the membership operator(.)

obj_name.var_name  / obj_name.function_name

"""

# EX 1:

class Student:        # decalring the class
    name = "manju"    # data member  / variable
    roll = 47         # variable
    role = "tester"   # Variable

    def attendence(self): # function 
        print("Student is present")
    def getData(self):
        print(f"{Student.name} is {Student.role}")

obj = Student() # Creating the object
obj.attendence()  # Calling the method
obj.getData()


# EX 2 :
class numbers:
    x = 10
    y = 20
    def getdata(self):
       print("hii hello welcome to the world")
ob1 = numbers()
print(ob1)
print("value of x before changing = ",ob1.x)
ob1.x = 52
print("value of x after changing =",ob1.x)
ob1.getdata() 