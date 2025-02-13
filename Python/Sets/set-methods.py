# Union:
"""union is a method that is used to combine the two sets without repeating the duplicate/repepated values.
Both union() and update() will exclude/not allows any duplicate items"""

set1={11,12,13,14,16,45,45,45}
set2={10,3,9,8,45,45,45,11,13,14}
print(set1.union(set2))

# update Method
"""update method is used to add the elements from the one set into current / another set 
==> updating is nothing but adding / appending the values from the one set to into the another set
==> like this we can update any type of sequences(list , tuple. dict..)  
"""
# EX 1: 
animals1={"dog","cat","rat",}       #type=set
print(animals1)
animals2=["pig","horse","monkey","deer"] # type= list
print(animals2)
animals1.update(animals2)#Updating the values from the list into set
print("after upadating the values from animals2 into the animals1 =",animals1)

# EX 2:
fruits1={"mango","grapes","banana"}
print(fruits1)
fruits2={"guava","orange","pomegranate"}
print(fruits2)
fruits1.update(fruits2)
print("after upadating the values from fruits2 into the fruits1 =",fruits1)

# intersection 
"""intersection is nothing but it returns the values which are common in the two sets.It returns only the common elements in both sets.."""
colors1={"red","cyan","blue","white","green"}
colors2={"white","green","yellow","pink"}
colors3=colors1.intersection(colors2)
print("common elements are: ",colors3) # it is returning into new set 

# intersection_update
"there is nothing so much difference between the intersection and intersection_update .i.e intersection returns into new set whereas the intersection_update  updates the values into the existing set from another set.."

"""returns only the duplicate values from set1 """

colors1={"red","cyan","blue","white","green"}
colors2={"white","green","yellow","pink"}
colors1.intersection_update(colors2)  # here it is only updating into exisitng set..
print("common elements are from intersection_update: ",colors1)

"""NOTE: there is nothing so much difference between the intersection and intersection_update .i.e intersection returns into new set whereas the intersection_update  updates the values into the existing set from another set..
Same thing applies to the Symmetric_difference and also difference.. """

# Symmetric Difference :

"""symmetric diference is nothing but it "returns the values that are not common/ not repeated in the both sets.."
==> it is simply quite opposite to the intersection ...
whereas intersection returns only the common elements / repeated values but symmetric difference returns not common values / non-repeated values"""

cities = {"kurnool", "kadapa", "nandyal", "banaganapalli"}
cities2 = {"kurnool", "Atmakur", "goa", "kadapa"} #here knl and kdp are repeated ...
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# Symmetric difference_update:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)



# difference
""" prints only items that are only present in the original set and not in both the sets.
 like A-B   common elements are removed from the setA and it returns the remianing valued from setA"""


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

# isdisjoint
"""it checks if items of given set are present in another set.
 This method returns False if items are present / common elements are present, else it returns True / if the commmon elements are not present.."""
cartoon1={"chotaBheem","Shinchan","doraeman","Ben10"}
cartoon2={"oggy and the cockroaches","He-man","Jackie-Chan"}
print(cartoon1.isdisjoint(cartoon2)) # returns true bcoz no elements are common in the sets
cartoon3={"chotaBheem","Shinchan"}
print(cartoon1.isdisjoint(cartoon3)) # returns false bcoz  elements are common in the sets

# issuperset:
"""The issuperset() method checks -->if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False."""

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Berlin"}
print(cities.issuperset(cities2)) # reutrns true bcoz all the elements in the cities2 are present in cities1 therefore cities is a superset of cities2
cities3 = {"Seoul", "Madrid","Kabul"} # reutrns false bcoz all the elements in the cities3 are not present in cities3 therefore cities is not superset of cities3
print(cities.issuperset(cities3))

# issubset():
"""The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False."""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# Add items
""""Once a set is created, you cannot change its items, but you can add new items.
=> we can add only one item at a time if u want to add multiple items then we have to use update method"""
animals={"dog","cat","rat","pig","horse","monkey","deer"}
print("Before adding =",animals)

animals.add("rabbit")
animals.add("cow")
print("After adding =",animals)


#remove Items
"""To remove an item in a set, use the remove(), or the discard() method.
===> 
we can remove the elements from the set in 3 types 
1.By using the remove method :Can remove the elements randomly by specifying the element name.If the sepecified element is not present in the list then it raises an error.

2.by using the pop method: can remove the item but we cant specify th element that to be deleted. It randomly deletes the element from the set.Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

3.by using the discard method:This is also used to remove the elements from the set.If the sepecified element is not present in the list then it raises an error

4. del method are used to delete the entire set

5. clear method is used to clear the values but not the set.."""

animals={"dog","cat","rat","pig","horse","monkey","deer"}

animals.remove("pig") #removes pig
print(animals)
# animals.remove("gorila") # raise an error

animals.discard("deer") #removes deer
print(animals)

animals.pop()
print(animals)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

cities.clear()
print(cities)

# Check if item exists
"""You can also check if an item exists in the set or not."""

sample = {"python", 19, False, 5.9}
if "python" in sample:
    print("python is present.")
else:
    print("python is absent.")