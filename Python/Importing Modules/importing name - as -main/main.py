import sample

print("this is the main file..")
sample.welcome()

print(__name__)  # sample file bcoz it is imported from any other file
                 # Initially it is imported from the sample.py file and it is executing the file therfore the __name__ will be Sample

