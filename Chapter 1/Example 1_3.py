# -*- coding: utf-8 -*-
"""
@author: guardati
Example 1_3
Printings in Python using the format() method.
"""

age = 83
# Print the text and the variable value occupying 5 spaces.
print('Grandfather’s age: {0:5d}'.format(age))  # Positional argument.   
print('Grandfather’s age: {age:5d}'.format(age = 88))  # Keyword argument.   

'''
The data indicated with 0 is replaced by the number 1 and the data 
indicated with 1, the number2 multiplied by 20. That is, first it 
multiply and the result is what is printed. Ten spaces are reserved 
and the result is printed right justify.
'''

number1 = 1258
number2 = 8920
# Positional arguments. 
print('{0:1d} {1:10d}'.format(number1, number2 * 20))  
# Keyword arguments.  
print('{number1:1d} {number2:10d}'.format(number1 = 1234, number2 = 987)) 
price = 2.23
# Leave 3 decimals: complete with 0.
print("El precio del pan es: ${0:.3f}".format(price))   
# Reserve 10 spaces for the number and justify right.
print("The price of bread is: ${0:10.3f}".format(price))   
print("The price of fruit is: ${fruit:.2f}".format(fruit = 4.5)) 

'''
In the first example, keyword arguments are used, since the name of the 
argument to be included in that position is presented between {}.
The second example uses positional arguments; that is, it is indicated 
by a number if it is to be replaced with the first data, second data, etc.
'''
print('This {tool} is {color} colored.'.format(tool = 'hammer', color = 'gray'))
print('This {0} is {1} colored.'.format('hammer', 'gray'))

# By using {0} twice, the word hammer is used in both positions.
print('This {0} is {0} colored.'.format('hammer', 'gray'))

'''
Example using variables instead of constants.
In this case only positional arguments can be used.
'''

animal1 = "cats"
animal2 = "dogs"
print('There is a belief that {0} and {1} cannot live together.'.format(animal1, animal2))
