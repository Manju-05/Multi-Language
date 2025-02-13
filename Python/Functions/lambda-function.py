# Lambda function:
"""
==> A lambda function is also known as 'anonymous function'.
==> In the normal functions we use the def keyword for the declaration / defination of the function.But in the lambda functions we use the lambda keyword and it doesnot have the function name therefore it is called as the anonymus function.
==> A lambda function can take "any number of arguments", but can only have one expression.
==> The power of lambda is better shown when you use them as an anonymous function inside another function.
==> Lambda functions are often used in situations where a small function is required for a short period of time. 
==> Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce. 
==> Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
"""
# syntax: lambda arguments : expression

# The lambda function should contain any number of arguements but only a single expression..


cube=lambda x:x*x*x   #returns the cube of the number...
print("cube of the number = ",cube(3))

average = lambda x , y :(x+y)/2
print(average(10,20))

square=lambda x:x*x   #returns the square of the number...
print("Square of the number = ",square(3))

# using the funciton inside another function
def function(f_name,value_of_sq):
    return 2 + f_name(value_of_sq)

result = function(square,2)  #calling the function inside another function..
print(result)