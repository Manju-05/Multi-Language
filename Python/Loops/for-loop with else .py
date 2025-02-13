# Python - else in Loop
"""As we know,that else clause is used along with the if statement.

Python also allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. 
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
The program exits the loop only after the else block is executed.

NOTE: The else block will NOT be executed if the loop is stopped by a break statement.
"""

# Syntax: 
"""for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block"""

for i in range(6):
    print(i)
else:
    print("else block is executed after the for looop")




# EX 2:
for x in range(8):
    if x == 4:
        print(x)
        break
else:
    print("exited from the looop")
