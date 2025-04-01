choices = ["🪨", "✂️", "📄"]

from os import system as terminal
from os import name


wins = 0
running = True
sudoMode = False

while running:
    terminal("cls" if name == "nt" else "clear")

    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice:")
    print("0: Rock (🪨)")
    print("1: Scissors (✂️)")
    print("2: Paper (📄)")
    print("3: Exit")
    if sudoMode:
        print("4: Add Wins | SUDO")
        print("5: Remove Wins | SUDO")
        print("6: Reset Wins | SUDO")

    choicesAvailable = 6 if sudoMode else 3

    print(f"Current wins: {wins}")
    choice = input(f"Enter your choice (0-{choicesAvailable}): ")

    if choice == "3":
        print("Exiting the game. Goodbye!")
        running = False
    elif choice == "4" and sudoMode:
        winsToAdd = input("Enter the number of wins to add: ")
        try:
            wins += int(winsToAdd)
            print(f"Wins added! Current wins: {wins}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "5" and sudoMode:
        winsToRemove = input("Enter the number of wins to remove: ")
        try:
            wins -= int(winsToRemove)
            print(f"Wins removed! Current wins: {wins}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "6" and sudoMode:
        wins = 0
        print("Wins reset! Current wins: 0")
    else:
        if choice in ["0", "1", "2"]:
            user_choice = choices[int(choice)]
            print(f"You chose: {user_choice}")

            import random
            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
                print("Try again.")
            elif (user_choice == "🪨" and computer_choice == "✂️") or (user_choice == "✂️" and computer_choice == "📄") or (user_choice == "📄" and computer_choice == "🪨"):
                print("You win!")
                wins += 1
            else:
                print("You lose!")
                wins -= 1
        elif choice == "admin activateSudo()":
            print("Sudo mode activated!")
            sudoMode = True
        elif choice == "admin deactivateSudo()":
            print("Sudo mode deactivated!")
            sudoMode = False
        else:
            print("Invalid choice. Please enter a number between 0 and 3.")

    input("Press Enter to continue...")