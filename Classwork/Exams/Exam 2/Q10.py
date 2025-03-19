# Question: Write a program that:
# 1. Asks the user how many colors they want to enter. 
# 2. Collects that many color names in a list. 
# 3. Prints the colors in alphabetical order.

colors = []

for x in range(int(input("How Many Colors Do You Want To Enter? "))):
    colors.append(input("Color?: \n "))
colors.sort()
print(colors)