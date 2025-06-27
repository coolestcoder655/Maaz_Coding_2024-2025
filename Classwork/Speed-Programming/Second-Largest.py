# Find the Second Largest Number in a List
# Do not use sort().

def secondLargest(i: list[int]):
    i = list(set(i))
    largest = float('-inf')
    secondLargest = float('-inf')
    
    # First Loop: Finding Largest
    for num in i:
        if num > largest:
            largest = num

    # Second Loop: Finding Second
    for num in i:
        if num > secondLargest:
            if num != largest:
                secondLargest = num

    assert secondLargest == sorted(i)[-2]