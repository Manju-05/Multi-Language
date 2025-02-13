# String formatting can be done in python using the format method.
"""In olden days string formatiing is done by using the .format() function 
It has lot of disadvanatages i.e when we use a lot of appendings --> {} <-- / in the middle of the sentence it becomes tooo difficult to handle. 
we append the literals or words in the middle of the sentence by using the .format() function  we can also specify the words by using index to be append"""

#This is the oldmethod that is used to format the strings

txt="my name is {} and i am from {}"
print(txt.format("Manjunath","India")) 

para="Hello {1} welcome to the {0} methods tut" #using index values to append
print(para.format("sython","jampandu"))#prints the values according to the index value order
print(para.format("jampandu","sython"))


# f-strings: 

"""It is also known as Literal String Interpolation or more commonly as F-strings   ==>(f character preceding the string literal).<== The primary focus of this mechanism is to make the interpolation easier
------------------------------------------------------------------------------------
When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.       """

name="Robo"
lang="java"
place="BPL"
study="dip"
hobbie="palyer"
print(f"Hello {name} welcome to the {lang} tutuorial Here f character is preceding the sentence")
x=(f"My name is {name} i am from {place} i am studying {study} i am a {hobbie} ")
print(x)


val = 'Geeks' 
print(f"{val}for{val} is a portal for {val}.")  

print(f"{2 * 30})")