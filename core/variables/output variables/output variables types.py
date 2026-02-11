'''The print() function is often used to output variables.'''
x = 'sree'
y = 2005
print(x)
print(y)

'''You can also output multiple variables in a single print() statement by separating them with commas.'''
print(x, y)

'''By default, the print() function outputs each variable separated by a space. You can change this by specifying the 'sep' parameter in the print() function.'''
'''You can also use the + operator to output multiple variables'''
x = 'dharma '
y = 2 
z = 'kushal '
print(x + str(y) + z)
print(x, str(y), z)
print(x, y, z, sep='-')

'''here at the first print this part 'print(x + str(y) + z)' there is a input int so it doesnt sepreate with space but in second print it separates with space because of comma operator.'''


'''For numbers, the + character works as a mathematical operator'''
a = 16
b = 2005
print(a + b)