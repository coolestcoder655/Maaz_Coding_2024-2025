# Write a Python program to combine two dictionary by adding values for common keys. 
from collections import Counter

count = {

}
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

# a = set(d1.keys()).intersection(set(d2.keys()))
# print(a)

# for x in a:
#     count[x] = int(d1[x] + d2[x])
    

# for x in d1:
#         count[x] = int(d1[x] + d2[x])
# print(count)

asd = Counter(d1)  + Counter(d2)
print(asd)