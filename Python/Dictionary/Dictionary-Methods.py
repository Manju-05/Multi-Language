# Dictionary Methods

# update()
"""The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
"""

info = {'name':'kajol', 'age':19, 'eligible':True}
print(info)
info.update({'age':20}) #if the key is already exist in the dict then the values are updated  else creates a new key pair value...
info.update({'DOB':2001})
print(info)

students1={
    1:"Ram",
    2:"Hanu",
}
students2={
    3:"Shiva",
    4:"Laxman",
    5:"Manju"
}
print(students1)
print(students2)
students1.update(students2)
#here we are updating the values of the student2 values into student1..
print("students1 after updating",students1)

# Finding the length:
print(len(students1))

# Removing the elements 

# pop():
"""
 ==> The pop() method removes the item with the specified key name
 ==> popitem() is used to delete the last key-pair value in the dictionary
 ==> clear() is used to clear the all the key pair values in the dict..
 ==>deletes the entire dictionary """
marks={
    "telugu":60,
    "hindi":70,
    "english":65,
    "maths":50,
}
print(marks)
marks.pop("dict after popping out maths =","maths")
print(marks)
marks.popitem()
print(marks)

marks.clear()
print(marks) # returns an empty dict '{}'

del marks["telugu"] #If key is not provided, then the del keyword will delete the dictionary entirely.
print(marks)

# del marks
# print(marks) # raises an error bcoz 'dict' is deleted 

# Copy a Dictionary
"""You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy()."""
dict = {
  "brand": "TATA",
  "model": "NANO",
  "year": 1964
}
mydict = dict.copy()
print("copy of dict by using the copy method",mydict)
duplicate=dict
print("copy of dict by using the = method",duplicate)

dict["milage"]=60
#here we are adding an another key-pair value to the dict but those changes will affect in the duplicate also bcoz it is created by using = method .and mydict wont effect bcoz it is cretaed by using the copy method..

print(duplicate)






