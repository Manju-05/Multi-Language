# Count Method:
""" The count() method of Tuple returns the number of times the given element repeated in the tuple. """

tup=(33.5,54,423,33.5,4323.43,33.5,33.5)
print(tup.count(33.5))

# index() method
""" ~ The Index() method returns the first occurrence of the given element from the tuple.
~ when u doesnot want the first occurence but u want to find in specific range of the value of the index.Then u have to use the following syntax.
Syntax: tuple.index(element, start, end) """

students=(12,78,96,78,55,"ramu","somu","hanu",12,"lakshman","veera","hanu")
print(students.index("hanu"))
print(students.index(12,3,9))

# finding the length of the tuple 
# we can find the length of the tuple by using the len() function
print(len(students))