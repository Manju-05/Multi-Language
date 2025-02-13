# 1.comments
# 2.types of comments
# 3.escape sequence characters
# 4.seperators
# 5.variables
# 6.rules for creating variables
# 6.types of variables.


# NOTE: comment:Comments can be used to explain Python code.
# The programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing. it is ignored by the interpreter


print("hey welcome to yhe pyhon tutorial  \n this is the example of sequence character here we cant enter to the new line without speacial character '\n' ")
# NOTE: types of comments

'''
hi 
hello
welcome   ---> these are the multi-line comments'''

#This is a 'Single-Line Comment'
print("This is a print statement.")

print("Hello World !!!")  #Printing Hello World

print("Python Program")
#print("Python Program")


# ESCAPE SEQUENCE CHARACTERS :

# \n :for new line
# \t :for tab space
# \"" : fro double quotations
# \' : for single quotations

print("\n")

# NOTE: seperators

#default separator=' ' 
# sep = "any symbol" add the specified symbol in the middle of the sentence
# end = "  " add the specified symbol in the middle of the sentence


print("hey", "user", "!", 12)
print("\n")

print("hey", "manju", "!", 12, end=' 321')

print("\n")
print("Hey", "I", "am", "manju", ".", "My", "age", "Is", 18, sep='_', end="9" "\n")


# NOTE: python variables

# variables: Variables are containers that store information that can be manipulated and referenced later by the programmer within the code.
# In python, the ""programmer does not need to declare the variable type explicitly, we just need to assign the value to the variable""".Python has no command for declaring a variable.A variable is created the moment you first assign a value to it.

name = "manju"       #type str
age = 20            #type int
result = True       #type bool
print("name of user is: " , name)
print("age is ",age)
print("result = ",result)

# checking the datatype of the varible
print("the datatype of name is ",type(name))
print("the datatype of age is ",type(age))
print("the result of age is ",type(result))

# NOTE: everything in the pyhton is an object.
# ---> rules to create variable
# It is always advisable to keep variable names descriptive and to follow a set of conventions while creating variables:

# Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable name must start with a letter or the underscore character.
# Variables are case sensitive.
# Variable name cannot start with a number.
Color = "yellow"    #valid variable name
cOlor = "red"       #valid variable name
_color = "blue"     #valid variable name

# 5color = "green"    #invalid variable name
# $color = "orange"   #invalid variable name


# NOTE : types of cases
 
NameOfCity = "Mumbai"     #Pascal case
nameOfCity = "Berlin"       #Camel case
name_of_city = "Moscow"     #snake case

#  NOTE:types of variables -->1.local variable  2. Global variable
# 1.local variables are declared within the function
# 2.Global Variables can be used anywhere within the code.

 
icecream = "Vanilla"    #global variable
def foods():  # declaring a function
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")
    print(icecream + " is a global variable value.")
    print(fruit + " is a local variable value.")

foods() # function call


print(icecream)  # Global variable acceses outside of the fuction
# print(fruit) # local variable can't access it throws an error
