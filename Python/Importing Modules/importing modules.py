# What is a Module?
"""A file containing a set of functions you want to include in your application.
For EX: sample.py userdefinedmoule.py,etc..."""

# Create a Module
"""To create a module just save the code you want in a file 
    with the file extension .py
"""
# How importing in python works ?
"""
==> Importing in Python is the process of loading code from a Python file / module into the another file / current script. This allows you to use the functions and variables defined in the another file / module in your current script, as well as any additional modules that the imported module may depend on.The main purpose of the imporiting is to reuse the code. We can import the builtin-modules and also the user-defined Modules..
==> To import a module in Python, you use the "import" statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions.
==> Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation.
"""

# importing the math builtin module using the square-root pre-defined function

# EX 1
import math
d = math.__doc__
print(d)
a = math.sqrt(49)  
print(a)
b = math.factorial(5)
print(b)
c = math.ceil(31.365484)
print(c)

# EX 2: importing the user defined module..
import sample
sample.greet()
print(sample.x)


# from keyword
""" sample.py file contains huge number of functions and the variables.. 
You can also import specific functions or variables from a module using the from keyword.
===> We should not use the module name infront of the function..""" 

# EX :importing only one function from the user-defined module
from sample import wish
wish()
# greet() ==> raises an error bcoz we doesnot imported the greet function from the sample module

# EX 2: importing only two functions from the math module
from math import pi, sqrt
print(pi)
print(sqrt(64))
# print(ceil(21.352136))   ==>  raises an error bcoz we doesnot imported the ciel function from the math module
# print(factorial(5432))   ==>  raises an error bcoz we doesnot imported the factorial function from the math module

# importing everything
"""It's also possible to import all functions and variables from a module using the '*'. wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from"""

# EX 2: importing all functions from the math module
from math import *
print(sqrt(323))
print(type(nan))

# The "as" keyword: 

"""Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.
For Ex : if the file name was too big to write so it is very difficult to perform the functoins and access the varibles by using the module name. so python allows u to rename the module by using the as keyword"""

# EX:without 'as' keyword
import userdefinedmodule
userdefinedmodule.display()

# EX:Renaming the user-defined module By using the 'as' keyword..
import userdefinedmodule as u
u.display()

# EX: renaming the pre-defined module
import math as m
print(m.sqrt(49))

#  dir function
""" 
==> Python has a built-in function called dir that you can use
==> To view the names of all the functions and variables defined in a module.
==> This can be helpful for exploring and understanding the contents of a new module."""
import math ,sample 
print(dir(math))
print(dir(sample))

"""This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants."""
