

# returns true when n1 < n2 < n3 < n4

def ascendingOrder():
    try:
        n1 = float(input("Please Enter A Number:"))
        n2 = float(input("Please Enter A Number:"))               # Asks a Float Input for length, width, and height
        n3 = float(input("Please Enter A Number:"))
        n4 = float(input("Please Enter A Number:"))
    except ValueError:
        print(f"{ValueError}, either n1, n2, n3, or n4 are not numbers. Please enter a number again.")
        exit
    if n1 < n2 < n3 < n4: 
        return True 
    else:
        return False
        
print(ascendingOrder())