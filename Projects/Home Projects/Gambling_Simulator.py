import random

jackpot = 0
guessingMachineTimesWon = 0
chips = 2000
slotChips = 0
hackingSoftwareActive = True

def guessingMachine(jackpot1):
    MAX = 2
    while jackpot1 != 10:
        number = random.randint(1, MAX)
        if hackingSoftwareActive == True:
            print("Activating Network Rerouter & Accsessing Servers \n Winning Number: ", number)
        print("Choose a number between 1 and ", MAX)
        userGamblingOption = int(input())
        if userGamblingOption == number:
            jackpot1 += 1
            MAX = MAX * 2
        else:
            jackpot = 0
    guessingMachineTimesWon += 1

        
def slotMachine(current_chips):
    winningSlot = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
    
    input("Press Enter To Spin...")
    slot = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
    print("Your Slot: ", slot, "\n Winning Slot: ", winningSlot)
    if slot == winningSlot or hackingSoftwareActive == True:
        current_chips += 15000
        return current_chips



while True:
    if chips < 0:
        print("You ran out of chips! Casino Security has forced you to leave the Casino.")
        break
    userChoice = input("Welcome to the Golden Unicorn Casino! \n Would you like to use the slot machine or the guessing machine? \n 1 = Slot Machine \n 2 = Guessing Machine \n 3 = Convert Chips into Cash & Exit \n ")
    try:
        if int(userChoice) == 1:
            while True:
                chips = chips - 100
                chips = slotMachine(chips)
                afterSlot = int(input("Would you like to keep playing to earn more money? \n Would you risk 100 chips to do so? \n 1 = Keep Going | Price = 100 Chips \n 2 = Stop"))
                if afterSlot == 1:
                    print(None)
                elif afterSlot == 2:
                    break
        elif int(userChoice) == 2:
            while True:
                chips = chips - 200
                guessingMachine(jackpot)
                print("JACKPOT!!!!!")
                afterJackpot = int(input("Would you like to keep going for more money and risk losing it all? \n Will you stop and keep the money you have? \n 1 = Keep Going | Price = 200 Chips \n 2 = Stop"))
                if afterJackpot == 1:
                    print(" ")
                elif afterJackpot == 2:
                    chips = guessingMachineTimesWon * 50000
                    break
        elif int(userChoice) == 3:
            print("Chips to Cash Converter: \n Conversion Rate: 5 Chips = 1 Dollar")
            print("Bank Account: \n $", chips / 5)
            break
    except:
        if userChoice == "Enable Hacking Software":
            hackingSoftwareActive = True
            print("Hacking Software Active \n HackME V1.08")
input()