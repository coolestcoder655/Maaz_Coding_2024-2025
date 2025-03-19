import random

options = ("rock", "paper", "scissors")
player = None
running = True

while running:
    computer = random.choice(options)  

    while player not in options:
        player = input("Enter a Choice (Rock, Paper, Scissors): \n ")

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("WINNER")
    elif player == "paper" and computer == "rock":
        print("WINNER")
    elif player == "scissors" and computer == "paper":
        print("WINNER")
    else:
        print("LOSER")
    
    if input("Play Again (Y / N)").lower() != "y":
        running = False