# FizzBuzz (Classic)
# Print numbers from 1 to 50. For multiples of 3 print “Fizz”, for 5 print “Buzz”, for both print “FizzBuzz”.

def fizzbuzz():
    is3 = lambda x: x % 3 == 0
    is5 = lambda x: x % 5 == 0

    
    def is3and5(x: int):
        if not x % 5 == 0:
            return False
        
        if not x % 3 == 0:
            return False
        
        return True

    for x in range(1, 51):
        if is3and5(x):
            print(f'FizzBuzz: {x}')
            continue
        elif is3(x):
            print(f'Fizz: {x}')
            continue
        elif is5(x):
            print(f'Buzz: {x}')
            continue

        print(x)
