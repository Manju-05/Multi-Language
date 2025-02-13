# # readlines() method
# """
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.
# NOTE: we use the read() it reads only a single charcter at a time.
#       wehereas when we use the readline() method it reads a single line at a time and returns in the form of list[]
# """
# # reading a single line
# f = open("file3.txt",'r')
# # f.write("This is file3 used for readlines() and writelines()")
# data = f.readline()  # reads only a single line from the file3
# print(data)


# # reading the mutiple lines using readline

# f = open('file3.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# # using readlines()
# f = open("file3.txt",'r')
# content = f.readlines() # reads all the content line by line at a time
# print(content)


# # reading the file by using the readline

# print("-------------------------------------------------------")
# file = open("file4.txt",'r') # opening the file4.txt
# i = 0
# while True:
#     i = i+1
#     line =file.readline()  # returns first line from the file4.txt
#     if not line:
#         break
#     m1 = line.split(",")[0]  # access the first element from the line
#     m2 = line.split(",")[1]  # access the second element from the line
#     m3 = line.split(",")[2]  # access the third element from the line
#     print(line)
#     print(f"student {i} marks in sub1 :{m1}")
#     print(f"student {i} marks in sub2 :{m2}")
#     print(f"student {i} marks in sub3 :{m3}")


# writelines() :
"""
==> The writelines() method  writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.
==> If we use the file.write() method we have to give the strings as a parameters  
==> If we use the file.writelines() method we have to give the sequence as a parameter"""


file = open("file5.txt",'w')
# file.write("1.This is the line1\n2.This is the line2\n3.This is the line3")
lines = ["1.This is the line1\n2.This is the line2\n3.This is the line3"] # this  is the sequence = (list) 
file.writelines(lines) 


