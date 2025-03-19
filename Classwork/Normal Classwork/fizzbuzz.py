# WAP to print numbers 1 - 50, multiplies of 3 print "Fizz", multiplies of 5 print "buzz", and multiples of 3 and 5, combine phrases

nums = range(1, 51)

for x in nums:
    if x%3 == 0 and x%5 == 0:
        print(f"FizzBuzz: {x}")
    elif x%3 == 0:
        print(f"Fizz: {x}")
    elif x%5 == 0:
        print(f"Buzz: {x}")