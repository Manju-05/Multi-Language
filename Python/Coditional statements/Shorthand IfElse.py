# If ... Else in One Line : 
"""
==> There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short
==> The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition.
==> It's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax."""

# if else condition Statement:
"""if condition:
    result = value_if_true
else:
    result = value_if_false"""

# Shorthand ifelse
""" result = value_if_true if condition else value_if_false """
# EX 1:
a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
print("a is greater than b") if(a>b) else print("equal Numbers") if a==b else print("b is greater than a")

# EX 2:
age=int(input("enter your age : "))
print("your are eligible") if(age>18) else print("you are not eligible..")

# And
"""The and keyword is a logical operator, and is used to combine conditional statements / check multiple conditions. and operator Returns true only if the both coditions are true else it skips the block.."""

# Biggest of three Numbers...

# x = int(input("enter the value of x"))
# y = int(input("enter the value of y"))
# z = int(input("enter the value of z"))
# if (x>y) and (x>z):
#     print("x is greatest")
# elif(y>x) and (y>z):
#     print("y is greatest")
# else:
#     print("z is greatest")

# Or
"""The or keyword is a logical operator, and is used to combine conditional statements / check multiple conditions. 
or operator Returns true if any one of the condition is true from the both coditions else it skips the block."""


# Not
"""The not keyword is a logical operator, and is used to reverse the result of the conditional statement:"""
