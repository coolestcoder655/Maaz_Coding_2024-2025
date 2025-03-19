import random

# Question: Write a function that:
# 1. Takes a list of numbers as input. 
# 2. Returns the smallest and largest numbers in the list. 
# 3. Prints both values.


numList = []

for x in range(10):
    numList.append(random.randint(0, 10))

def MinMax(x):
    x.sort()
    print(x[0], x[-1])

print(numList)
MinMax(numList)