# What is a data type ?
""" Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error."""

# 1. Numeric data: int, float, complex
# 2. Text data: str
# 3. Boolean data:True & False ("T & F should be capital")
# 4. Sequenced data: list, tuple
# 5. Mapped data: dict


a = 1
print("value of a=",a)
print(type(a))

b = "manju"
print("value of b=",b)
print(type(b))

c=True
print("value of c=",c)
print(type(c))

d=complex(23,32)
print("value of d",d)
print("type of d is",type(d))

e=321.321
print("value of e",e)
print("type of e is",type(e))

# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]  #MUTABLE-modifiable
print(list1)
print(type(list1))   

# tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))  #IMMUTABLE-can't modified
print(tuple1)
print(type(tuple1))   


# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

dict={"name":"Sakshi", "age":20, "canVote":True}
print(dict)
print(type(dict))   
