# WAP to multiply all the items in a dictionary.

a = 1

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4
}

for x in nums.values():
    a = x * a

print(a)