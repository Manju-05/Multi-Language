# DocSrings PEP 8

# DocStrings:
"""Python docstrings are the string literals that appear right after the definition of a function, method, class, or module."""

# Example 1

def display():
    '''this is the function of displaying the values of the type str'''
    x=input("Enter anything...!")
    print(x)
display()

print(display.__doc__) # This is the attribute that returns the doc stirng content


# Python Comments vs Docstrings

# Python Comments
"""Comments are descriptions that help programmers better understand the content and functionality of the program. They are -->completely ignored<-- by the Python interpreter."""

# Python docstrings
""" Python docstrings are ---->strings used right after the definition of a function, method, class, or module <---- (like in Example 1). They are used to document our code.
--->We can access these docstrings using the doc attribute."""

# Python doc attribute
"""Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.

=====> Syntax:  function-name.__doc__   """

# example 2:
def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)

# example 3:
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and
    does not do anything interesting, except for illustrating
    what the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.
    """
    return num1 + num2
print(add.__doc__) 



# PEP 8
""" PEP 8 is a document that provides guidelines and best practices on how to write Python code.PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community. 

==> This is the Do-Nothing statement just like lorem in html it is a collection of words...!"""

import this  #Do this in the python REPL
             # 1. Go to DOS prompt 
             # 2. And enter ---->  python 
             # 3. Enter ---->  import this 
             # 4. Then  click ---> enter
 
