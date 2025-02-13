# Else Keyword..
"""You can use the else keyword to define a block of code to be executed if no errors were raised """
# EX 1:
try:
    a = int(input("enter a number :"))
    b = int(input("enter another number :"))
    print("sum of two numbers is = ",a+b)
except Exception:
    print("Invalid input")
else:
    print("no error are occured program was sucessfully fininshed..")

# Raise an exception
"""As developer you can choose to throw an exception if a condition occurs.
In python library there will be some of the builtin exceptions / predefined Exceptions.. like- nameError , ValueError , IndexError ,MemoryError , IndexOutofRange ,typeerror , unreferenced error, etc.. These will automatically raises when we make any mistake.

But what if especially u have to check the specific condition and u have to raise the error if it become false 

For EX: U want to check the eligibity of the person to votee..
if the user is above 18 then he is eligible if less than 18 then we have to raise the error explicitly..

if u want to throw an error when certain conditions are fails then we can throw an explicit error..

To throw (or raise) an exception, use the "raise" keyword.
"""
# EX 2:
age = int(input("enter Your Age : "))
try:
    if(age>18):
        print("Your are eligible to vote..!")
        print("your voter details are : ")
        print("your name is: User 1 ")
        print("your mobile number is: xxxxx 98032 ")
        print("your adhar  number is: 2312 xxxx 5421 ")
    else:
         raise Exception("Not Eligible to vote")
except ValueError:
        print("Invalid Input..")

# EX 3:
num=int(input("enter postive Integer : "))
if(num<0):
     raise Exception("Invalid Input.. Enter +ve number..!")
else:
     print("Entered Number is : ",num)
