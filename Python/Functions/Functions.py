# What is a function ?
"""A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat."""

# Types of Functions?
"""  There are two types of functions:
1.Built-in functions
2.User-defined functions """


# Built-in functions:
"""These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc."""

list=[2,133,12,3,324,32,3,4,4545,345,6,43,2,3,254,3534,32,34,43,523,4]
hobby="coding"
print("Smallest number =",min(list))
print("Biggest number =",max(list))
print("length of string",len(hobby))
print("data-type of is =",type(hobby))
 #like these are the some of the built-in functions that are provided by the python library.

# 2.UserDefined function
""" userdefined funcitons are the functions that are defined by the user explicitly as per the user need.
Syntax:     def fucntion-name(paramters):
                // body of function / statements to be executed 

Here "def" is a keyword that is used to declare a function 
Function name is the name of the function
Paraneters are the optinal as per the user need
Then the body of the function """

# Calling a function:
"""We call a function by giving the function name, followed by parameters (if any) in the parenthesis.
  syntax:  function_name(parameters) """

# calculation of two numbers
def calculate(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    mod=a%b
    exp=a**b
    print("Addition of the two numbers",add)
    print("subtraction of the two numbers",sub)
    print("Multiplication of the two numbers",mul)
    print("division of the two numbers",div)
    print("modulus of the two numbers",mod)
    print("exponent of the two numbers",exp)
calculate(12,65) #function call



