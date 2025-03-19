# Create a tuple fruit_tuple with the values "apple", "banana", and "cherry". Use tuple unpacking to assign each fruit to a separate variable, and then print each variable.

fruitTuple = ("apple", "banana", "cherry")

# one = fruitTuple[0]
# two = fruitTuple[1]
# three = fruitTuple[2]

# Better Approach

one,two,three = fruitTuple

print(one)
print(two)
print(three)