# what is tuple?
""" ~ Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets () or paranthesis.
~ Tuples are immutable.
~ Tuples are unchangeable meaning we can not alter them after creation.
NOTE: if there is nothing inside the parnthesis then it is empty tuple but 
if u insert only one integer value then it is not tuple it is int"""

tuple=(1) #you should use comma to represent this as a tuple
tuplez=()
print(type(tuple)) 
print(type(tuplez)) 

tuple1 = (1,2,2,3,5,4,6,)
print(tuple1)

# tuple1[2]=47 #appending the value 47 at the index 2
                #throws an error bcoz tuples are the immutable we cant perform any    changes on it.

""" NOTE:Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple

===> Here intially we converted the tuple2 into list by holding it in a temp variable and then we perform the operations on the temp variable after performing all the operations and then we converted into the tuple by assinging it the tuple2. """

"""
tuple2 = ("Red", "Green", "Blue")
print(tuple2)
print(type(tuple2))

temp=list(tuple2)
print(type(temp))
temp.append("apple")
temp.append(456)
print(temp)

tuple2=tuple(temp)
print(type(tuple2))  """

# Tuple Indexes:

""" Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.
 ==> Positive Indexing:
As we have seen that tuple items have index, as such we can access items using these indexes. positive indexes ranges from left to right."""

# country = ("Spain", "Italy", "India",)
# #            [0]      [1]      [2]     
# print(country[0])
# print(country[1])
# print(country[2])

#  ==> Negative Indexing:

"""Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on. negative indexes ranges from right to left."""

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])

# Check for item:

"""We can check if a given item is present in the tuple or not. If the specifies element id present in the tuple then it returns true else it returns false.This is done using the in keyword."""

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

 # Range of Index:
"""You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

# Syntax:  Tuple[start : end : jumpIndex]"""

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])    
print(animals[-7:-2])  
print(animals[1:8:3])
    
#Packing and unpacking of Tuples
"""packing a Tuple:
When we create a tuple, we normally assign values to it. This is called "packing" a tuple"""
student = ("01", "Manju", "CME")
print(student)
# Unpacking a Tuple:
(rollno, name,branch ) = student
print(rollno,name)