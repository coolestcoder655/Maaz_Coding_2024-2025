"""
i = 1

while i <= 100000:
    print("Iteration", i)
    i += 1

i = 5

while i < 6:
    print("Iteration", i)
    i -= 1
"""

# i = 1

# while i <= 100:
#     print(i)
#     i += 1

# i = 100

# while i >= 1:
#     print(i)
#     i -= 1

# n = 2
# b = 0

# while b != 12:
#     print(n * b)
#     b += 1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0

# while i != len(nums):
#     print(nums[i])
#     i += 1

# from random import randint

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = randint(0, len(nums))
# i = 0
# while i != x:
#     print("Nope")
#     i += 1

# print("Found it!", nums[x])


# i = 0

# while i != 10:
#     if i == 4:
#         i += 1
#         continue
#     print(i)
#     i += 1

# nums = (1, 2, 3)
# for x in nums:
#     print(x)
#     break
# else:
#     print("End of Program")


# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for x in nums:
#     print(x)

# from random import randint

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# a = nums[randint(1, len(nums))]

# for x in nums:
#     if x == a:
#         print(f"{nums.index(a)} is the index of the number {x}.")
#         break

# for x in range(101):
#     print(x)

# for x in range(100, 0, -1):
#     print(x)

# i = 6

# for x in range(1, 12):
#     print(i * x)


# x = int(input("Number: "))
# i = 1
# numSum = 0

# while i <= x:
#     numSum = numSum + i
#     i += 1

# print(numSum)

x = int(input("Number: "))
numSum = 1

for i in range(1, (x + 1), 1):
    numSum = numSum * i
print(numSum)