# # List Methods
# """1.append
# 2.sort
# 3.reverse"""

# # 1.Append:
# """This method appends items to the end of the existing list."""
# # animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# # print("before appending",animals)
# # animals.append("kothi")
# # print("before appending",animals)

# # 2.sort:
# """This method sorts the list in ascending order. The original list is updated
# What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method."""

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# numbers=[32,43,24,54,87,234,1]
# animals.sort()
# numbers.sort(reverse=True) #prints in descending order
# print(animals)
# print(numbers)

# # reverse()
# """This method reverses the order of the list."""
# ex=[423,45,76,79,8967,12,5,3,232,3,4,564,67,6]
# ex.reverse()
# print(ex)

# # index()
# """This method returns the index-number of the first occurrence of the list item."""
# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.index("green"))
# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.index(3))

# # count()
# """Returns the count of the number that is repeated how many times."""
# x=[32,32,32,32,32,453,6,5,76,875,3,634,5]
# print(x.count(32))

# # copy()
# """Returns copy of the list. This can be done to perform operations on the list without modifying the original list."""

# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)

# # insert():
# """This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method."""

# colors = ["voilet", "indigo", "blue"]
# #           [0]        [1]      [2]
# colors.insert(1, "green")   #inserts item at index 1

# # updated list: colors = ["voilet", "green", "indigo", "blue"]
# #       indexes             [0]       [1]       [2]      [3]

# print(colors)

# # extend():
# """This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list."""

# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors) 

# Concatenating two lists:
"""You can simply concatenate two lists to join two lists."""

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)