# Taking User Input in python 
"""  In python, we can take user input directly by using ""input()"" function.This input function gives a return value as string/character hence we have to pass that into a variable """

# Syntax
variable_name=input("Enter the sample text :")
# But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

Username=input("Enter the name: ")
print("Welcome to the tutoral",Username)

x=input("Enter the value of x :")
y=input("Enter the value of y :")
print("sum of a , b = ",x+y) # Here  it adds combines the number bcoz input function accepts the string values only we have to type-caste them
print("sum of a , b =",int(x)+int(y))
print(type(x))

x=int(input("Enter the value of x :"))
y=int(input("Enter the value of y :"))
print("sum of a , b = ",x+y) # Here  it adds  the number bcoz input function accepts the string values and converts them into the integer values with the help of the int();
print("sum of a , b =",int(x)+int(y))
print(type(x))

