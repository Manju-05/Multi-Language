# Opening a File: open()
"""
Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.
"""

# Modes in file : Read() Write() and append()
"""
read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

write (w): This mode opens the file for writing only and creates a new file if the file does not exist.If the file already exists then it overwrites the content in the file.

append (a): This mode opens the file for appending only and creates a new file if the file does not exist.And add the content at the end of the existing content instead of overwriting it.
"""

# Reading from a File
"""The read() method reads the entire contents of the file and returns it as a string. If the file doesnot exits then it will throw an error."""

f = open("file1.txt",'w')   #creates a file named = file1.txt
print("file is created sucessfully..!")
f = open("file1.txt",'r')
content = f.read()  # reads the content in the file
if(content == "") :
    print("empty file...!")
else:
    print(content)


# Writing to a File
"""To write to a file, we first need to open it in write mode."""

f = open("file1.txt",'w')
f.write("This is the content that is written through the write method..") # If the file doesnot exist then it creates and writes the content to the file. else it overwrites the content in the file.
print("content is added sucessfully..")

# append :
"""If you want to append the content at the end of the file instead of overwriting it, you can open it in append mode."""

f = open("file1.txt",'a')
f.write("This is the content that is append through the append method to the file.")
print("content appended sucessfully")

# Closing a File
"""It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access"""

f2 = open("file2.txt",'') # creates a file2.txt 
f2.write("Hey this is the another file..!")
f2 = open("file2.txt",'r') # reads the file2.txt 
print(f2.read())
# print(f2.read(12)) # returns only 12 characters from the file.. 
# f2 = open("file2.txt",'a')
# f2.write("Hey this is the additional content that is added to the file2.txt by using append mode..")
# f2.close()