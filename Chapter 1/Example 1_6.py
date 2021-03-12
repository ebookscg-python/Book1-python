# -*- coding: utf-8 -*-
"""
@author: guardati
Example 1_6
Examples of dynamically variable typing.
The 2 variables used have an associated type, depending on the value assigned.
"""

number = 45  # An integer value is assigned.
print('\nVariable \"number\" is of type: ', type(number))   

number = 45.16  # A real value is assigned.
print("It's modified! Now \"number\" is of type: ", type(number))   

pet_name = "Nera"  # A string is assigned.
print('\nVariable \"pet_name\" is of type: ',type(pet_name))   

pet_name = True  # A boolean value is assigned.
print("It's modified! Now \"pet_name\" is of type: ", type(pet_name))   

