# -*- coding: utf-8 -*-
"""
@author: guardati
Example 1_7
Reading (entering) data through the keyboard.
"""

print("\nWhat's your name? ")  # The name is requested through a print().
name = input()

# Place of residence is requested including a message in the input().
city = input("Where do you live? ")

# Age is requested. In this case it will be necessary to convert
# the data entered to integer.
age = int(input("How old are you? "))

# Height is requested in meters. The data entered is converted into a real number.
height = float(input("How tall are you - in meters? "))

# All the data read is displayed.
print(f'\nThe person with the name {name} lives in {city}. He is {age} years'
      f' old and his height is {height} m.')