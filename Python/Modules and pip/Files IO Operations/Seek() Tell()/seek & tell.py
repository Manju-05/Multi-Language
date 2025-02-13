# seek() function
"""
==> The seek() function allows you to move the current position of the filepointer to a specific point. 
==> The position is specified in bytes, and you can move either forward or backward from the current position.      """
# tell() function : 
"""
==> The tell() function returns the current position within the file, in bytes. 
==> This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position.       """
# truncate() function: 
"""
==> If you want to truncate the file to a specific size, you can use the truncate function.
==> If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file.       """

 # Example for tell() operation 

file = open("sample.txt",'w')  # creates the sample file
print(type(file))
line = file.write("hello world") # writes the data in sample.txt

print("The current file position = ",file.tell()) # returns the current file pointer position
file = open("sample.txt",'r') 
print(file.read())

# Example for seek operation

file = open("sample.txt",'r') # opens in reading mode
file.seek(6) # sets the file position to the 6 byte
print("File pointer current position after seeking()",file.tell())
data = file.read()  # reads the data from the 6 byte position
print(data)
# data = file.read(3) # reads 3 bytes from the 6 byte position
# print(data)


f = open("sample2.txt",'w')
f.write("Hey this is the example of truncate function")
f.truncate(20) # allocates only 20 bytes of the space only to the sample2 file

f = open("sample2.txt",'r')
print(f.read())