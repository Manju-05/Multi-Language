# Python Lists
""" ~ Lists are ordered collection of data items.where the List items are separated by commas and enclosed within square brackets [].
~ They store multiple items in a single variable.
~ list is a mutable datatype i.e-lists are changeable => we can alter them after creation.
~ list elements are indexed. so they can accesed by using the index. Index will be either positive or negative 
~ From left to right positive index & From right to left it is negative"""

# List Index
"""Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on."""

# Accessing list items
"""We can access list items by using its index with the square bracket syntax [].
Positive Indexing Negative Indexing..."""

list1=[4234,34,234,324,"manju",True,432,"Delhi"]
print(list1)
print(type(list1))
print(list1[0])
print(list1[7])
print(list1[-4])

# Check whether an item in present in the list?
"""We can check if a given item is present in the list. This is done using the memebership operators (in) (not in) keyword."""

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

# Range of Index:
"""You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.
Syntax: listName[start : end : jumpIndex]"""
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:])
print(animals[::-1])  #reverse the list 
print(animals[:6])    #using positive indexes
print(animals[:-3])	  #using negative indexes
print(animals[::2])	  
print(animals[1:8]) 
print(animals[1:8:3]) 

# List Comprehension
"""List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
With list comprehension you can do all that with only one line of code
newlist = [expression for item in iterable if condition == True]"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits]
newlist2 = [x for x in fruits if "a" in x]
print(newlist1)
print(newlist2)