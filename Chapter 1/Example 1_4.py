# -*- coding: utf-8 -*-

"""
@author: guardati
Example 1_4
Printings in Python using f-strings.
"""

age = 83
print(f'Grandfather is {age} year’s old.')

value = 'height'
height = 1.72   
print(f'Grandfather’s {value} is {height:.1f} m.')  # Gives format to the number.

name = 'Albert'
print(f"My grandfather's name is {name}.")

# The !r causes the name value to be written between ''.
print(f'I told you his name is {name!r}.')  # 'Albert' will be displayed.

# With < 10 you reserve 10 spaces for the variable value.
format11 = f'{value:<10} = {height:.2f}' 
print(format11)

format2 = f'{value!r:<10} = {height:.2f}'  
print(format2)

# Example combining f-string with string format.
format3 = f'{"weight".capitalize()} = {59.605:.2f}'  
print(format3)
