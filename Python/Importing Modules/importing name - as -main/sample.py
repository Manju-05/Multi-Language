def welcome():
    print("Hi hello welcome to the importing of module concept..")
    print("this is the sample module..")

if __name__ == "__main__":
    welcome()
    print(__name__)  # __main__  bcoz it is not imported from any other file
                     # Initially it is not imported from any other files and it is executing the main file therfore the __name__ will be main

"""if __name__ == __main__ then the funtion is executing from this file only i.e
(main.py file ) if __name__ is not equal to __main__then the function in the main file wont be executed.."""


# DOCUMENTATION: 
    
# if "__name__ == "__main__" in Python
    
"""The ==> if __name__ == "__main__" <== idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script."""
"""
==> The __name__ variable is a built-in variable that is automatically set to the name of the current module.
==> When a Python script is run directly, the __name__ variable is set to the string __main__ 
==> When the script is imported as a module into another script, the __name__ variable is set to the name of the module."""

# Why is it useful?
"""
==> This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script
==> If you run this script directly, it will output "Hi hello welcome to the importing of module concept..""this is the sample module..
==> However, if you import it as a module into another script and call the main function from the imported module, it will not output anything
==> This can be useful if you have code that you want to reuse in multiple scripts, but you only when u want it to run. And not when it's imported as a module.

"""
# Is it a necessity?
"""However, the if __name__ == "__main__" idiom can be a useful tool for organizing and separating code that should be run directly from code that should be imported and used as a module.
==> for suppose assume that u r imported a module. And this module contain a function which deletes all your files in your current working folder.So when u only imported the module and u doesn`t make any funtioncall() .But also the module that u r imported will executes automatically (bcoz the function which is defined in the module have a functioncall()... when u import it automatically Executes the function) and deletes all the files
"""
