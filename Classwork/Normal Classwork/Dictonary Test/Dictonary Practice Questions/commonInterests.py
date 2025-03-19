# 6.	Find Common Interests:
# Given two sets of favorite hobbies from two friends, find their common hobbies.

friend1 = {"Python", "Reading", "Traveling", "Swimming"}
friend2 = {"Python", "Gaming", "Cooking", "Swimming"}

"""
for x in friend1:
    if x in friend2:
        print(x)
"""
commonHobbies = friend1.intersection(friend2)
print(commonHobbies)