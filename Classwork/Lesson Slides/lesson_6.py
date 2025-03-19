def length(lists):
    print(len(lists))

def elements(elements):
    for x in elements:
        print(x, end= ", ")

def factorials(factor):
    i = 1
    for x in range(1, factor + 1):
        i = i * x    
    return i

def converter(USD):
    # 1 USD - 85.693 INR
    return USD * 85.693

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    print("End")

def sum(n):
    if n == 0:
        return 0
    else:    
        return sum(n - 1) + n

def sumLoop(n):
    i = 0
    for x in range(1, n + 1):
        i = i + x
    print(i)
    return

def showList(toPrint, index):
    if index == 0:
        return toPrint[0]
    else:
        print(toPrint[index])
        return showList(toPrint, index - 1)

numList = [10, 9, 8, 7, 6]

def FIBONACHISEQUENCE(num):
    if num == 2 or num == 1:
        return 1
    else:
        return FIBONACHISEQUENCE(num - 1) + FIBONACHISEQUENCE(num - 2)

FIBONACHISEQUENCE(5)


def main():
    name = "Maaz"
    index = len(name)-1
    print(name)
    def reversestring():
        nonlocal index
        print(name[index], end="")
        index = index - 1
        if index >= 0:
             reversestring()
    reversestring()


def power(num, toThePower):
        return num ** toThePower



def recursivePower(num, toThePower):
    a = 10
    if toThePower == 0:
        return 1
    else:
        print(num)
        return num * recursivePower(num, toThePower - 1)

print(recursivePower(2, 3))