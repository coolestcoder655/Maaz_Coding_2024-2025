from random import randint

class Solution:
    def __init__(self):
        self.number = randint(1, 100)

    def HotorCold(self, num):
        if self.number < num:
            return "Lower!"
        elif self.number > num:
            return "Higher!"
        elif self.number == num:
            return True

guess = Solution()
notRunning = False
testing = True

while not notRunning == True:
    if testing:
        print(guess.number)
    temp = guess.HotorCold(int(input("Enter a Number: ")))
    if temp == True:
        notRunning = True
    else:
        print(temp)

print("You Win!!")