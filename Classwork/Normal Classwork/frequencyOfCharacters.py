# WAP to take a string input from the user and calculate the frequency of each character using a for loop

string = input("Enter a String to Check: ")
uniqueString = set(string)


for x in uniqueString:
    print(f"{x}: {string.count(x)}")