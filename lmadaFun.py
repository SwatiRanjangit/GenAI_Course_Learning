'''
lambda functions are anonymous functions defined using lambda keyword. they can have any no of arguments but only one expression.
functions without name.

#Syntax:

lambda arguments: expression


addition=lambda a,b:a+b
print(addition(5,5))

even = lambda num: num%2==0

print(even(12))
'''
'''
MAP- applies a function to all items in a list

syntaxt: map(expression , iterables)
'''

numbers=[1,2,3,4,5]

squared_num = list(map(lambda x:x**2, numbers))
print(squared_num)


