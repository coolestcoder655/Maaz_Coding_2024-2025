# Question: Write a program that:
# 1. Takes two lists of numbers from the user. 
# 2. Combines them into a single list. 
# 3. Removes duplicates from the combined list. 
# 4. Sorts and prints the final list.

list1 = []
list2 = []
combinedList = []



for x in range(5):
    list1.append(int(input("Please Enter A Number For The First List:")))
for x in range(5):
    list2.append(int(input("Please Enter A Number For The Second List.")))

for x in list1:
    combinedList.append(x)
for x in list2:
    combinedList.append(x)

for x in combinedList:
    if combinedList.count(x) > 1:
        combinedList.pop(combinedList.index(x))

combinedList.sort()

print(combinedList)