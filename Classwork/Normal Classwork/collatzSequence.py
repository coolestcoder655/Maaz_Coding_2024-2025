# WAP to generate a Collatz Sequence for any positive number


a = int(input("Give Me A Number: "))

while a > 1:
    if a%2 == 0:
        a = a / 2
    else:
        a = (a * 3) + 1
    print(int(a))