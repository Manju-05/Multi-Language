# What is conditional Statements?
""" Sometimes the programmer needs to check the evaluation of certain expression's, whether the expression's evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path then it would have if the expression had evaluated to True.
Based on this, the conditional statements are further classified into following types; if, if……else, elif, nested if.   """

# Conditional Operators : < , > , <= , >= , == 

# Indentation:
"""  In other programming languages like c,c++,java we use the curly braces {} to display or write a block of code.But python doesnot supports the braces it uses the indentation to represent a block of code.indentation is nothing but whitespace at the beginning of a line to define scope in the code. if u don't use the indentation python throws an error."""

# if Statement:
""" Execute the block of code inside if statement if the expression evaluates True.
if the condition is evaluated true then body of if block is executed if condition is false then the control gets out of the block of code(if block). and rest of statements are executed."""

age=int(input("Enter your age :"))
print("your age is :",age)
if(age>=18):
    print("you are eligile to drive / vote")
    print("Hi i am inside block")
print(" I am out of the block")

# if-else:
"""Execute the block of code inside if statement if the expression evaluates True.
Execute the block of code inside else statement if the expression evaluates false"""

age=int(input("Enter your age :"))
print("your age is :",age)
if(age>=18):
    print("you are eligile to drive / vote")
    print("Hi i am inside if block")
else:
    print("you are not eligile to drive / vote")
    print(" I am inside else block")

# elif:
"""Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement."""

num = int(input("enter the number :"))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")
print("I am out of Block")

# Nested if Statement
"""We can use if, if….else, elif statements inside other if statements."""
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")