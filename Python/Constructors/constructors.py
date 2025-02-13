# Constructors :
"""
==> Constructors are the speacial methods that are used to  used to create and intialize the values to the variables / fucntions or object of that class.
==> The constructors will automatically invokes whenver the object is created.
==> A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.
==> __init__ is one of the reserved functions in Python and also known as double underscored function. In Object Oriented Programming, it is known as a constructor.
==> It accepts a default parameter i.e, self

NOTE : In oops Concepts every 'function' and the every 'constructors' default value is 'self'.

"""
# Syntax of Constructor

"""
def __init__(self):
	# initializations

"""
# Types of constructors :
"""
IN python there are two are two types of constructors :
1. Default constructor
2. Parameterized constructor"""

# Default Constructor in Python
"""
When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor. also when the user doesnot specify any constructor then the compiler will automatically creates a default constructor with null value.
"""

class Details:
    # def __init__(self):
    #     print("Hey this is the default constructor.")
    
    print("Helloworld")
info = Details()

""" NOTE :Here the constructor will automatically invoked whenever the object is created.   """


# Parameterized Constructor
"""
When the constructor accepts arguments along with self, it is known as parameterized constructor.

These arguments can be used inside the class to assign the values to the data members.
"""

class cars:
    demoPiece = "Nano"
    bike = "jupiter"

    def __init__(self , brand , model , year ,price):
        self.br = brand
        self.mo = model
        self.yr = year
        self.pri = price

def getdata(self):
        print(f"brand = {self.brand} model = {self.model} year = {self.year} price = {self.price}")

toy = cars("Tata" , "punch", 2020 , '$15')
print(toy.demoPiece)

toy2 = cars("Mahindra" , "Scorpio" , "2021" , "$44")
print(toy2.bike)


class exams:
     def __init__(self, m1 , c , python ,java):
          self.maths = m1
          self.c = c
          self.python = python
          self.java = java
     def display(self):
            print(f"marks -> maths = {self.maths} c = {self.c} python = {self.python} java= {self.java}")

result = exams(10,25,32,45)
result.display()

result2 =exams(15,65,48,32)
result2.display()
          




