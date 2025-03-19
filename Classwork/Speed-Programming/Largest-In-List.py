# WAP to find the largest number in a list.

numList = [70, 2, 5, 100, 120, 67]


max = numList[0]

for x in numList:
    if x > max:
        max = x

print(max)
