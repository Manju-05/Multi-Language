# What is variable ?
"""
==> A variable is a named location that stores a value. we assign the values to the variables by using the assignment operator "=" .
"""
# local varible:
"""
==> A local varible is a variable that is declared within the function and it can be accessed within that function only.
==> It cannot accesed from the outside of the funtion and anywhere execpt within the function only.
==> The local variable creates when the function is called and it is destroyed when the function returns."""

# Global varible :
"""
==> A Global varible is a variable that is declared outside of the function and it can be accessed from anywhere in the program.
==> It can accesed from the outside of the funtion and anywhere in the program.
"""
# Example:
fruit = "Appple" #global variable

print(f"{fruit} is a global variable. And it can be accesed from anywhere in the program")
def vehicles():
    x = "car"   #local variable
    y = "bike"  #local variable  
    print(f"{x} {y} are local varibles. And it can accesed within this function only.")
vehicles()

print(fruit) #this is the global variable and accesing from the outside of the function. 

# sample programme :
icecream = "Vanilla"    #global variable
def foods():  # declaring a function
    vegetable = "Potato"    #local variable
    print(vegetable + " is a local variable value.")
    print(icecream + " is a global variable value.")
foods() # function call

print(icecream)  # Global variable acceses outside of the fuction
# print(vegetable) # local variable can't access it throws an error

# The global keyword :
"""what if we want to modify a global variable from within a function? This is where the global keyword comes in.

The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope"""

var1 = 47 # global 
def example():
    global var1 
    var1 = 66
    print(f"value of var1 = {var1} after changing from inside of  the variable")
example()
   
