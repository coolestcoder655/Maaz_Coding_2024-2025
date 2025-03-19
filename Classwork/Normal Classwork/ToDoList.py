# WAP that allows a user to add tasks, view the list and remove completed tasks.

tasks = []


while True:
    userChoice = int(input("What would you like to do? \n 1 = View the List \n 2 = Add An Item \n 3 = Remove a Task \n 0 = Close Application"))
    lentasks = len(tasks)
    
    if userChoice == 1:
        print(tasks)
    elif userChoice == 2:
        x = input("Please type your task here:")
        tasks.append(x)
    elif userChoice == 3:
        print(tasks)
        y = int(input("Please enter the task to be removed: (Please use numbers 1, 2, etc...)"))
        if y != len(tasks):
            print("Sorry, there are only", lentasks, "items inside the To-Do list. Please choose a value between 0 and", lentasks)
        else:
            tasks.pop(y - 1)
    elif userChoice == 0:
        break
    else:
        print("Please enter a number: 1 \n 2 \n 3")
