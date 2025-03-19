# Question: Write a program that asks for a person's age and calculates the ticket price using the following criteria: 
# children (below 12) = $5, adults (13-59) = $12, seniors (60 and above) = $8.

childTicket = 0
adultTicket = 0
seniorTicket = 0

tickets = int(input("How many tickets are you planning to purchase?: "))

while tickets != 0:

    answer = int(input("Please write your age?: "))

    if answer <= 12 and answer >= 1:
        childTicket = (childTicket + 1)
        print(" + $5")
    elif answer > 12 and answer <= 59:
        adultTicket = (adultTicket + 1)
        print(" + $12")
    elif answer >= 60:
        seniorTicket = (seniorTicket + 1)
        print(" + $8")
    else:
        print("Please put your age, and make sure that the number is only digits and greater than 1.")
        tickets = (tickets + 1)

    tickets = (tickets - 1)



print(f"You are paying a total of {(childTicket *  5) + (adultTicket * 12) + (seniorTicket * 8)} dollars.")