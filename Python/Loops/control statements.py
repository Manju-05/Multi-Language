# Control Statements
"""There are three control statements that can be used with for and while loops to alter their behaviour.

They are pass, continue and break."""

# 1.Break :
""" break is a keyword that is used to exit from out of the loop whenever a specific codiotion meets..break keyword is used to bring the control out of the loop and into the main body of the program. Whenever the break keyword is used, the loop is terminated and the control starts executing the next series of statements within the main program."""

# for i in range(10):
#     # print(i,i+1)
#     i=i+1
#     if(i==8):
#         print("condition is matched ")
#         break
#     print(i)
# print("out of the loop main body")


# 2.continue:
"""his keyword is used in loops to end the current iteration and continue the next iteration of the loop. Sometimes within a loop, we might need to skip a specific iteration. This can be done using the continue keyword."""

# for i in range(0,5):
#     if(i==3):
#         continue
#     print(i)


#  pass:
""" pass is a do nothing statement that does nothing . it is used to create an empty blocks .Whenever loops, functions, if statements, classes, etc are created, it is needed that we should write a block of code in it. An empty code inside loop, if statement or function will give an error. 
~Pass is used when the user declare a function but not yet defined so empty function may genereates an error therefore we use the  keyword pass"""
    
# i = 1
# while (i<5):  # generates an error bcoz while is the empty block: expected an indented block after 'while' statement

i=0
while (i<=10):
    pass
 