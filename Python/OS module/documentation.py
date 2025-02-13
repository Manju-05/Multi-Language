import os
# OS Module in Python 
"""The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.

Some important functions of the Python os module :

==> Handling the Current Working Directory  jgfwe
==> Creating a Directory  jgfwe
==> Listing out Files and Directories with Python  jgfwe
==> Deleting Directory or Files using Python"""  

# directory= folder

# Creating a Directory

# for creating the single folder
os.mkdir("OS module/sample.txt") 
print("sample.txt folder created")

# For creating the multiple directories at a time..
for i in range(0,10): 
    print(f"creating New Files from 1 to 10 in the data folder =")
    os.mkdir(f"OS module/data/New File{i+1}")
    print(f"{i+1} folder is Created..")

# To get the current wroking directory
print("The current working directory = ",os.getcwd()) # returns the path of the folder


# Changing the Current working directory
print(os.getcwd())   # retuns : D:\SIGMA  COURSE\Python
os.chdir("OS module/data")  #changing the path to : OS module/data
print(os.getcwd())  # retunrs : D:\SIGMA  COURSE\Python\OS module\data
print(os.listdir()) # returms all the files in the data folder.. ==> from New File1 to New File10

# Listing out Files and Directories with Python
print(os.getcwd())
print(os.listdir("OS module/sample"))  # returns all the list of files in this path..

# Deleting Directory or Files  
"""
Using os.remove()
Using os.rmdir()
"""
# To delete the files os.remove()
"""Steps to delete the file :
1. store the path of the file in a variable
2. store the filename in a variable 
3. join it by using the join method
4. And then delete it by using the os.remove() method """

path = "OS module/sample/"
file = 'New File9.txt'
path =  os.path.join(path, file) 
os.remove(path) 
print(f"{file} from {path} is deleted")

# To delete the directory (folder) we will use==>  os.rmdir()

print(os.getcwd())
folder= "Duplicate"
path = "D:/SIGMA COURSE/python/OS module/"
path = os.path.join(path , folder)
os.rmdir(path)
print(f"{folder} from {path} folder is deleted..!")

# File Operations..
"""
# Store the file in a variable..
1.open the file
2. read/ write the file 
3.close the file"""

os.chdir("D:/SIGMA COURSE/python/OS module/") # changing the path directory to this files path 
 
fd = "GFG.txt"
file = open(fd, 'w')
file.write("Hello welcome to the file operations ")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
file.close()


# renaming a file 

os.chdir("D:/SIGMA COURSE/python/OS module/")  # changing the path directory to this files path 
print("renaming the file from GFG.txt to file-operations.txt")
os.rename(f"manju3.txt",f"Manju47.txt")
print("File is Renamed....")
os.remove("Example.py")
print("Example.py is deleted")
