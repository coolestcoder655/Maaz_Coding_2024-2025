# You are given the following list of numbers:

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Write a Python function that:

# 1. Removes all duplicates from the list.

# 2. Sorts the list in ascending order.

# 3. Returns the updated list.

numbers = [1,1,5,8,9,5,3,7,8,10,100]

# 3 1 4 5 9 2 6

def countandpop(x):
    if numbers.count(x) > 1:
        numbers.pop(numbers.index(x))


for x in numbers:
    print(numbers.count(x))

numbers.sort()

print(numbers)