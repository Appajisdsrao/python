'''Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. However, if you create a variable outside of a function, it is global, and can be used anywhere in the code.'''
'''1.Global variables can be accessed from any function, but they cannot be modified inside a function unless you use the global keyword.'''
def myfun():
    global x
    x = 'sree'
myfun()
print('deepak and ' + x + ' are friends')

'''2.To change the value of a global variable inside a function, refer to the variable by using the global keyword, followed by the variable name.'''

y = 'dharma'
def my_fun():
    global y
    y = 'kushal'
my_fun()
print('dharma and ' + y + ' are friends')