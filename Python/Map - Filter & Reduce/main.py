# Map, Filter and Reduce :
"""
In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments."""

# map :
"""
==> The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
==> The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object."""

# SYNTAX :
""" NOTE : map(function_name, iterable / sequence)   """

#  sample function WITHOUT MAP FUNCTION..
def cube(x):
    return x*x*x
# print(cube(2))  #Function call

# NOTE : what if we want to apply the function to the no.of elements in the list[].We will use the for loop.
"""
list = [2,6,8,3,4,7,5,2]
print("cube of elements in list =")
for i in list:
    print(cube(i))
"""
# BY USING THE MAP FUNCTION :

li = [2,6,8,3,4,7,5,2]
newl = []
# newl = map(cube,list) # when we use like this it returns the map object.
newl = list(map(cube,li))
print("map function using function :",newl)

# OR WE CAN USE THE LAMBDA FUNCTION ALSO IN THE MAP FUNCTION
tup = (2,3,4,5,6,7)
square = tuple(map(lambda x : x*x , tup))
print("map function using the lambda :",square)

# filter :
"""
The filter function filters a sequence of elements based on a given predicate / condition (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate/ condition."""
# NOTE : SYNTAX : filter(predicate, iterable)
def fun_filter(a):
    return a>40

numbers = [23,25,57,45,48,16,23,37,85,45,65]
print("Filter =Numbers > 40 :")
print(list(filter(fun_filter,numbers)))

# reduce
"""The reduce function is a higher-order function that applies a function to a sequence and returns a single value."""

# NOTE : SYNTAX :  reduce(function, iterable)
"""
==> The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple."""
"""
==> The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.
--> NOTE : if u want to use the reduce function then u have to
                 ==> import the reduce"""

from functools import reduce
numbers = [1,2,3,4,5] #  1+2 =3 3+3=6 6+4=10 10+5=15
result = reduce(lambda x,y :x+y , numbers)
print(result)

# Working of function :
"""The lambda function adds the two arguments x and y and returns the result. The reduce function applies the lambda function to the first two elements in the list (1 and 2), then applies the function to the result (3) and the next element (3), and so on. The final result is the sum of all the elements in the list, which is 15."""