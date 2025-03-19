"""
    *
   ***
  *****
 *******
*********
"""

global number
number = 15

objects = 1

for x in range(1, number + 1):
    spaces = number - x
    print((" " * spaces), (objects * "*"))
    objects += 2