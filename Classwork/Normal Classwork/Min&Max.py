# Question: Write a function that:
# Takes a list of numbers as input.
# Returns the smallest and largest numbers in the list.
# Prints both values.


def minMax(num_list):
    print("The smallest number is ", num_list[0], "and the largest number is", num_list[-1])

num = []

for x in range(10):
    numToAdd = int(input("Please enter the number to add: "))
    num.append(numToAdd)

num.sort()

minMax(num)