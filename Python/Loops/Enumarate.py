# Enumerate function
"""The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time"""

# Syntax: 

"""enumerate(iterable, start=0)
Parameters:

Iterable: any object that supports iteration
Start: the index value from which the counter is to be started, by default it is 0
Return: Returns an iterator with index and element pairs from the original iterable"""

# These are the normal for loop iterations..

i = 0
fruits=("mango","grapes","banana","apple","custardmelon")
for i in fruits:
    print(i)
i = 1+1

fruits=("mango","grapes","banana","apple","custardmelon")
for i in fruits:    #prints all the items of the list..
    print(i)

fruits=("mango","grapes","banana","apple","custardmelon")
for i in range(0,len(fruits)):  #prints indices of the list
    print(i)

# enumerate Function.. (to print both at a time indices and the items)
    
fruits=['apple', 'banana', 'mango',"custardmelon"]
for fruit in enumerate(fruits):
    print(fruit)


# Changing the start index:
"""By default, the enumerate function "starts the index at 0", but you can specify a "different starting index" by passing it as an argument to the enumerate function"""

# Loop over a list and print the index (starting at 1) and value of each element
"""NOTE:Here the elements wont start from the specified index but the default-
index 0 will start from the specified start value.."""

fruits = ["mango","grapes","banana","apple","custardmelon"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# loop through the string by iterating..

greet= 'hello'
for i in enumerate(greet):
    print(i)