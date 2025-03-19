# Question: Given a tuple numbers_tuple = (5, 10, 15, 20), do the following:
# 	1.	Convert the tuple into a list.
# 	2.	Add the number 25 to the list.
# 	3.	Convert the list back into a tuple and print the updated tuple.

numbersTuple = (5, 10, 15, 20)

a = list(numbersTuple)

a.append(25)

c = tuple(a)

print(c)

# Question: You have a list animals = ["cat", "dog", "rabbit"] and a tuple birds = ("sparrow", "eagle", "parrot"). Combine both into a new list called creatures and print the result.

animals = ["cat", "dog", "rabbit"]

birds = ("sparrow", "eagle", "parrot")

creatures = animals + list(birds)

print(creatures)