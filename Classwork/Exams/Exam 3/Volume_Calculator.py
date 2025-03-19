
# l * h * d = v

def volumeCalculator():      # Calculates Volume With l(length), w(width), and h(height) by multiplying. Returns That Value To Be Stored or Printed
    try:
        length = float(input("Please Enter The Length of The Shape:"))
        width = float(input("Please Enter The Width of The Shape:"))               # Asks a Float Input for length, width, and height
        height = float(input("Please Enter The Height of The Shape:"))
    except ValueError:
        print(f"{ValueError}, either length, width, or height are not numbers. Please enter a number again.")
        exit
    return length * width * height


print(volumeCalculator())       # Prints Returned Value of volumeCalculator()