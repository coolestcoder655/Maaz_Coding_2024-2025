# WAP to sum all items in a list.

numberList = []
sum = 0
multiplySum = 1
while True:
    x = int(input("1 = Add An Item | 2 = Check Items in List | 3 = Add All Numbers | 4 = Multiply All Numbers"))

    if x == 1:
        itemToBeAdded = int(input("Item to be Added:"))
        numberList.append(itemToBeAdded)
    elif x == 2:
        print(numberList)
    elif x == 3:
        for i in numberList:
            sum = sum + i
        print(sum)
    elif x == 4:
        for y in numberList:
            multiplySum = multiplySum * y
        print(multiplySum)
    else:
        break