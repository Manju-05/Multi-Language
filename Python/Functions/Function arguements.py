# Function Arguments and return statement
""" There are four types of arguments that we can provide in a function:

~ Default Arguments
~ Keyword Arguments
~ Variable length Arguments
~ Required Arguments """

# 1.Default arguments:
"""We can provide a default value while creating a function. whenever the user does not provide the value in the function call then the default arguements are taken."""

def sum(a=23,b=2):
    result=a+b
    print("sum of ", a , "+",b,"=",result)
sum()
sum(90,99)
sum(10)
sum(b=67)
    
# 2.Keyword arguments:
"""We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter"""
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Gandhi", lname = "Tatha", fname = "Mahatma")
name(lname="Ramarao" ,mname="Taraka", fname="Nandamuri")

# Required arguments:
"""In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments the number of arguments passed should match with actual function definition."""

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

# name("Gandhi", "Tatha")  rises an eror bcoz we defined a function with 3 parameters but we called with only 2 parameters 

# Arbitrary Arguments:
"""Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple."""

def display(*numbers):
    print(numbers)
display(32,32,3,)#function call
display(32,32,3,23,12,3,13,1,23,)# like this we can call with any number of arguements
display(32,32,3,23,12,3,13,1,23,1,3,213,12,3,1,3,543,4,5,34,)


# return Statement:
# return statement means returning the control to the back to the executuion cntext wehere the function was invoked....i.e from the functioncall() and rest of the statements wont executed..
"""The return statement is used to return the value of the expression back to the calling function.
Once you declare a return statement the next statements wont execute"""
def sample(a,b):
    print("sum",a+b)
    return a+b
    return a*b
    return a%b
sample(32,3)
