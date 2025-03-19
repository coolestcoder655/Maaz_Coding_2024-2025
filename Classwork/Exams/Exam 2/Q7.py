# • Question: Given the following list of items:
# Write code that:
# 1. Slices the list to get the middle three items. 
# 2. Reverses the entire list. 
# 3. Prints both the sliced and reversed lists.

items = [
    "apple",
    "banana",
    "cherry",
    "date",
    "fig", 
]

middleItems = []

middleItems.append(items[1])
middleItems.append(items[2])
middleItems.append(items[3])

items.reverse()

print(middleItems)
print(items)