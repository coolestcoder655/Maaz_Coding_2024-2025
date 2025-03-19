for x in range(2, 7, 1):
    y = 0
    while y != x:
        if y == 0:
            print("", end="")
        else:
            print(y, end=" ")
        y += 1
    
    print("")