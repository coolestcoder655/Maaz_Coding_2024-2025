# WAP to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
list123 = ["aba", "1221", "as", "aslkdalsjdlk", "aaa", "a"]

num = 0
results = []
trues = 0
falses = 0
for x in list123:
    check = list123[num]

    if check[-1] == check[0] and len(check) > 1:
        results.append("True")
        trues = trues + 1
    else:
        results.append("False")
        falses = falses + 1
    num = num + 1
    
print(results)
print("There is a total of ", falses, "and a total of ", trues, "inside all of the array.")