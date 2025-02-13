# Difference between "is" & "==" 
"""
==> In python is both 'is' and '==' operators are used to check if two values are equal or not.
==> The 'is' operator is used to check the identity (address of values or reference of the value)of the two objects. 
==> While the '==' operator is used to check /compare the values of the objects.
==> This means that 'is' will only return True if the objects being compared are the "exact same object in memory", while '==' will return True if the objects "have the same value"
==> For mutable objects such as lists and dictionaries. 'is' and '==' can behave differently. In general, you should use '==' when you want to compare the values of two objects, and use "is" when you want to check if two objects are the same object in memory.
"""

# is operator on tuple => tuple will always return true bcoz the tuple values are immutable.
tup1 = (2,3,4,5)
tup2 = (2,3,4,5)
print("operations on tuple")
print(id(tup1))  # returns memory-reference / adddress of the variables
print(id(tup2))
print(tup1 is tup2)
print(tup1 == tup2)

#  is operator on list values will return false bcoz the list values are mutable.
li1 = [2,3,4,5]
li2 = [2,3,4,5]
print("operations on list")
print(id(li1))
print(id(li2))
print(li1 is li2) 
print(li1 == li2)


# in python strings are immutable therefore the strings returns true.
str1 = "CSE"
str2 = "CSE"
print("operations on strings")
print(str1 is str2)
print(str1 == str2)

#  is operator on dictionary values will return false bcoz the dictionary values are mutable.

dict1 = {"college":"sv" , "roll": 47 , "bus-no" : 2}
dict2 = {"college":"sv" , "roll": 47 , "bus-no" : 2}
print("operations on dictionaries")
print(dict1 is dict2)
print(dict1 == dict2)


a = 47
b = "47"
print("comparision b/w strings and number")
print(a is b)
print(a == b)

x = 50  # if we assign like this then the compiler of python       automatically identifies as tuple values. These values are mutable therefore they return true.
y = 50
print("comparision b/w constants")
print(x is y)
print(x == y)

z = None
zx = None
print("comparing with None")
print(z is zx)
print(z is None)
print(z == zx)


"""
Conclusion : 

==> To get a clear overview use the id(var_name) fucntion which returns the memory-referernce/address of the varaible.

==> If we compare the values of the "mutable objects" (list , dictionary and etc..) then the 'is' operator will "return false" and '==' operator will "retrun true.

==> If we compare the values of the "immutable objects" then the "both is and == operator will return true".  
==> when we assign the same values in the immutable objects then it stores the values in the same memory location and doesnot creates the another copies of the values." 

"""