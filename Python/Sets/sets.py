# Sets
"""
==> Sets are unordered collection of data items.(the order of the data will be changes everytime when u run the program).
==> They store multiple items / different data-types in a single variable. 
==> Set items are separated by commas and enclosed within curly brackets {}. 
==> NOTE: if u want to create an empty set then u have to use the set() function instead of => {} if we use the curly braces then it returns the dict datatype.
==> Sets are unchangeable, meaning you cannot change items of the set once created. 
==> Sets do not contain duplicate items.
==> The items of set occur in random order and hence they cannot be accessed using index numbers.
==> False and 0 is considered the same value:
==> True  and 1 is considered the same value:

"""

set1 = {"Ramu", 19, False, 5.9, 19,0} # 0 is not printed bcoz false is considered as 0
print(set1)
print(type(set1))

example={12,12,13,14,12,12,12,12,True,1.1,1,1,1} # it does not prints the repeated values it doesnot allows the duplicate values..
# 1 is not printed bcoz true is cosidered as the 1
print(example)


# empty_set={} returns dict
empty_set = set()
print(type(empty_set))



# aceesing the list items:
""" The items of set occur in random order and hence they cannot be accessed using index numbers."""
for i in set1:
    print(i)

animals=set(("cow","rabbit","horse","deer")) 
#creating the sets by using the set constructor with double rounded braces===>(())
print(animals)
print(type(animals)) #returns set
