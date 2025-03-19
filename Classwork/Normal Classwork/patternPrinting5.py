"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

global number
number = 5

objects = 1

for x in range(1, number + 1):
    spaces = number - x
    print((" " * spaces), (objects * "*"))
    objects += 2
    

for x in range(number + 1, 0, -1):
    spaces = number - x
    print((" " * spaces), (objects * "*"))
    objects -= 2
    

"""
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********



  *       *
 * *     * *
*   *   *   *
     *       *