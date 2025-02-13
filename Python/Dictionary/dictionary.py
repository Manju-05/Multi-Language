# Dictionary
"""Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
Dupicates are not allowed..
keys cant be duplicate but values can be duplicate"""

students={
    1:"Ram",
    2:"Hanu",
    3:"Shiva",
    4:"Laxman",
    5:"Manju"
}
#accesing the values of the dictionary by using the keys

print(students) # aceess whole keys and values
print(students[3]) #acess only the key-value if the value is not present then it raise an error
print(students[1])
print(students.get(5)) #acess the key-value if the value is not present then it doesnot raise an error it gives NONE output

# Accessing multiple keys and values:

"""We can print all the keys & values in the dictionary using keys  and values() method."""
students={
    1:"Ram",
    2:"Hanu",
    3:"Shiva",
    4:"Laxman",
    5:"Manju"
}
print(students.keys())
print(students.values())

# Accessing key-value pairs:
"""We can print all the key-value pairs in the dictionary using items() method."""
students={
    1:"Ram",
    2:"Hanu",
    3:"Shiva",
    4:"Laxman",
    5:"Manju"
}
# print(students.items())

# loop through dictionary

for x in students.keys():
    print(x)
    
for y in students.values():
    print(y)

for x,y in students.items():
    print(x, y)
