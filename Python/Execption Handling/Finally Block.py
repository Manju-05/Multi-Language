# Finally
"""The finally block will Executes ,regardless if the try block raises an error or not.
Case 1: If  error occur in try block then the control goes to the Except block and the finally block is executed..
Case 2:Error is not occured in try block then it skips the Except block and the finally block is executed.."""

"""NOTE:Finally Block main purpose whenever we write some function and return something in the function then the rest of the statements wont execute after the return satement. If u want to ecxecute the some of the statements after the return then we have to use the finally block.."""

def func1():
  try:
    list = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(f"{i} indexed vaulue is: ",list[i])
    return 1
  except:
    print("Some error occurred")
    return 0
  finally:
    print("I am always executed")
# print("out of the program..")

x = func1()
print(x)

# EXAMPLE:

# age = int(input("enter Your Age : "))
# try:
#     if(age>18):
#         print("Your are eligible to vote..!")
#         print("your voter details are : ")
#         print("your name is: User 1 ")
#         print("your mobile number is: xxxxx 98032 ")
#         print("your adhar  number is: 2312 xxxx 5421 ")
#     else:
#          print("Not Eligible to vote")
# except ValueError:
#         print("Invalid Input..")
# finally:
#      print("finally block is Executed...!")
#      print("Out of the program..")
#      print("Some of the IMP code...")
     

