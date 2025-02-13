# Recursive functions:
"""
==> Which means a defined function can call itself.It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
==> Be very careful with recursion as it can be quite easy to slip into writing a function which never terminates.
==> We know that a function can call other functions. It is even possible for the function to call itself

# factiorial of a given number 

def factiorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factiorial(n-1) 
        # calling the function repeatedly in the function..until it satisfies the condition..
    
print(factiorial(3))"""



# Formula to Find Fibonacci Numbers : Fn = Fn-1 + Fn-2 

def fibonacci(n):
    if(n<=1 ):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))


