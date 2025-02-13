print("hey welcome to typeCasting tutorial")

# What is casting?
""" Casting is the process of converting the data from one type to another.There may be times when you want to specify a type on to a variable.  """

# Types pf casting
""" 1. Implicit Conversion  (Automatically)
    2. Explicit Conversion  (Manually by the user)  """
   
# These are the variety of ""functions""" or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.



# implicit conversion  
"""It will automatically converts the datatype & the main condtio is that the intial source data should be less than the destination """

a=10 # int
b=29.5  # float
result=a+b      # Int + Float = Float
print("Sum of a , b =",result)
print(type(result))

# Explicit conversion (Done manullay by specifying the datatype)
number = 7
string = "15"
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
print(type(sum))
