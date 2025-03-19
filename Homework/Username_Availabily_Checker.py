# WAP that takes a username as input and checks whether it’s available (i.e., not in the predefined list of taken usernames).

usernames = []
# ShadowFox42", "CosmicNinja99", "PixelWizard101", "n0tH1ngSp3c14l", "Wh4t3v3rM4n

while True:

    userToBeAdded = input("Welcome to the Username Availabilly Checker \n Please enter the username to be cross-refrenced.")
   
    userToBeAdded = userToBeAdded.strip()

    if (userToBeAdded in usernames):
        print("Sorry, the username chosen is inside the database and therefore cannot be used.")
    else:
        print("Your account has been created and your username has been stored.")
        usernames.append(userToBeAdded)
        print(usernames)

