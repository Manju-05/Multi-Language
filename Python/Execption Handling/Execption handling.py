# Exception handling :
"""
==> Execption is the unexpected event that  prevents / stops the execution of the program abnormally at runtime / compiletime.
 ==> Exception handling deals with these events to avoid the termination. exception handling is used to execute normal operation of a program.
==> Inorder to handle the execptions we use the try execpt blocks.."""
# Python try...except
"""
==> try except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.
==> We can use multiple except blocks in the single try block or we can also use the nested except block 
==> while using the multiple or nested except Blocks NOTE:: The default Exception class(super class) should be sepcified at last."""

# syntax 
"""try:
     #statements which could generate exception
except nameError:
     #Solution of generated exception
except ValueError:
     #Solution of generated exception
except IndexError:
     #Solution of generated exception
except Execption:
     #Solution of generated exception"""

# EX 1:
a = int(input("enter the number:"))
b = int(input("enter the another number:"))
c= a+b
print(c)
# when the user tries to enter the string format values in a or b then the error raises and program termiantes abnormally..

# EX 2:
try:
    a = int(input("enter the number:"))
    b = int(input("enter the another number:"))
    c= a+b
    print(c)
except:
    print("Invalid input.. Try again..!")
print("out of the programm..")
print("some of the imp code running...")

"""if the error occur in the try block then the control goes to the except block 
if the error not occur then the control will skips the except block and jumps out of the block 
So by this the program will not terminate abnormally it catches the error and handles it.. and also the rest of the statements will execute.."""

# types of exceptions...
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]   # array holding of size 1 if try to access out of rang then it will raises an errr...
    print(a[num])

except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")

#   if we give the invalid number i.e string format value error error raises if we gives the range of above 1 then it will raises index error..
  
# EX 3:
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid  Input!")

print("out of the Block")
print("Some imp lines of code")
print("End of program")