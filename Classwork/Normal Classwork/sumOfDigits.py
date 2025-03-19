# WAP to take a number as an input and calcutate the sum of its digits using a while loop

number = int(input("Number?: "))
numSum = 0


while number > 0:
    numSum = numSum + (number%10)
    number = number // 10
print(numSum)