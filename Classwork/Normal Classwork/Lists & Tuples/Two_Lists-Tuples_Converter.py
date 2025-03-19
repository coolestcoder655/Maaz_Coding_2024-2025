# Question: Given a tuple num_tuple = (8, 3, 7, 1, 9), write code to:
# 	1.	Convert the tuple to a list.
# 	2.	Sort the list in ascending order.
# 	3.	Convert the list back to a tuple and print the sorted tuple.


numTuple = (8, 3, 7, 1, 9)
numList = list(numTuple)

numList.sort()

numTuple2 = tuple(numList)

print(numTuple2)