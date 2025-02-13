# what is string?
""" A string is a sequence fo charaacters that are enclosed between single or double qoutes  or triple quotes"""

name="manju"
print(name)
print(type(name))

description=""" hi
this is the multilne text
we can enter multiple lines within the triple quotes"""
print(description)

# whenever we want use the single or double quotes within the quotes then we have to use some of the special characters like escape sequence characters
"""
# \n : for new line
# \t : for tab space
# \"": fro double quotations
# \' : for single quotations 
# \\ : Backslash
# \r : Carriage Return
# \b : Backspace  """

print('hiiii "welcome to the tutorial"')
print("hello user welcome to the \"python\" tutorial")
print("hey this is the \texample ") #for tab space
print("hello i am  __ age \nThis is the new line in python")# for new line

# String Slicing 
"""Slicing:  Slicing can return a range of characters
   Syntax:   variable(start:stop)
   start index and the end index, separated by a colon  """
x="national anthem"
print(x[0:]) #from 0 index  to end
print(x[:9]) #from start to 9 index character
print(x[:-4]) #here negative index starts from right-hand-side
print(x[-4:]) #Here negative index starts from negative index
#Acessing the strings :it can be accesed by index --> string is like an array of characters. We can access parts of string by using its index which starts from 0.
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

#acces through loops
name="abcdefgh"
for i in name:
    print(i)

# String Methods
"""Stirngs are immutable"""

#Finding the length of a string
fruit = "!!!Mango!!!!!"
print("length of a fruit is :",len(fruit))
print(fruit.upper())  # converts lower to upper
print(fruit.lower())  # converts upper to lower
print(fruit.strip("!")) #removes the ! mark from both side
print(fruit.rstrip("!")) #removes the ! mark from right side
print(fruit.lstrip("!")) #removes the ! mark from left side
x="Hi user welome to the python tutorial user thanks user"
print(x.replace("user","manju"))  # replaces the names
#split() :The split() method splits the given string at the specified instance and returns the separated strings as list items.
str2 = "Silver Spoon"
print(str2.split(" ")) 

# capitalize() :The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
y="code with random"
print(y.capitalize())

# count() :returns the number of times the given value has occurred within the given string.
vehicle="lorry"
print(("no of times r is repeated",vehicle.count("r")))

# endswith() :The endswith() method checks if the string ends with a given value.If yes then return True, else return False.
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

# find() :searches for the first occurrence of the given value and returns the index where it is present.
str1 = "His name is Dan. He is an honest man."
print(str1.find("is"))

# index() method searches for the first occurrence of the given value and returns the index
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
# isalnum() :only consists of A-Z, a-z, 0-9.BUT NOT SPEACIAL CHARACTERS
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
# isalpha() :
"""only consists of A-Z, a-z. BUT NOT NUMBERS AND SPEACIAL CHARACTERS"""
#  islower() :
"""method returns True if all the characters in the string are lower case, else it returns False."""
# isprintable():
""" method returns True if all the values within the given string are printable, if not, then return False."""
# The isprintable():
""" method returns True if all the values within the given string are printable, if not, then return False. \m \t cannot printable """
#  isspace():
""" method returns True only and only if the string contains white spaces, else returns False"""
#  isspace() 
""" method returns True only and only if the string contains white spaces, else returns False"""
# istitle() :
""" returns True only if the --first letter of each word of the string is capitalized--, else it returns False. -->for ex:World Health Organization     """
# isupper() :
"""method returns True if all the characters in the string are upper case, else it returns False."""
# startswith() :
"""method checks if the string starts with a given value. If yes then return True, else return False."""
# swapcase() :
"""method changes the character casing of the string. --Upper case are converted to lower case and lower case to upper case--."""
#  title() 
"""method capitalizes each letter of the word within the string."""




