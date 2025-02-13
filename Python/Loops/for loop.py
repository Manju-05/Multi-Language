# Loops:
"""Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following types; for loop, while loop, nested loops."""

# for loop :
"""for loop is mainly used whenever the user know to number of repititoins are going to be happen for ex : 100 times , 5 times , 10 times until a specfic condition satisafies that block of statements are going to be executed / or
 --loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries."""

# iterating over a stirng

name = 'Manjunath'
for i in name:
    print(i,end=",")
print("iterating a string")    
print("\n")

# iterating over a list tuple dictionary

list1=["manju","banana","apple","cars","fruits"]
for element in list1:
    print(element,end=",")
print("iterating a list")    
print("\n")

tuple1=(1,2,23,34,4,5456,6564,345,47)
for num in tuple1:
    print(num,end=",")
print("iterating a tuple")  
print("\n")


ex=[2,123,213,2354,454,6,342,123,3123,4324,543,5354,]
for i in ex:
    if(i>7950):
        print(i)
    else:
        print("NOB")


# like in the other languages for loop they will have like for(i=0;i<n;i++)
"""But in python language we have intialize the index number first and then the condition and atlast the increment or decrement operation"""

index=0
sample=[234,24.23,231313,4324,432,321,3131,324324,325435,23424123,]
for index in sample:
    print(index)
index += 1


    



# What if we do not want to iterate over a "sequence"? What if we want to use for loop for a specific number of times?
"""Here, we can use the range() function"""
""" syntax : range(start,stop,step)
    start :specifies the start number (default is 0)
    stop : specifies the ending number this will be (n-1)
    step : specifies the increment of the numbers """

for i in range(10):
    print(i+1)
for i in range(1,10):
    print(i)
for i in range(0,25,2):
    print(i+1)
for i in range(0,25,3):
    print(i+1)

