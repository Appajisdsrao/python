'''1.The variables that are defined in the main body of a Python file, outside of any function or class, are called global variables. They can be accessed and modified from anywhere in the code, including inside functions and classes'''
x = 'sree'
y = 2005
def my_fun():
    print(x + str(y))
my_fun()
'''In the above code, x and y are global variables. They can be accessed from inside the function my_fun() and also from outside the function.'''


'''2.Create a variable inside a function, with the same name as the global variable'''
x = 'sree'
def my_function():
    x = 'sameer'
    print('kushal and ' + x)
my_function()
print('kushal and ' + x)