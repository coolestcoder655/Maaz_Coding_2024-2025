# formula:
#   A = P(1+4/n)^t

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the Prinicple Amount: \n "))
    if principle <= 0:
        print(ValueError)
while rate <= 0:
    rate = float(input("Enter the Rate Amount: \n "))
    if rate <= 0:
        print(ValueError)
while time <= 0:
    time = int(input("Enter the Time Amount: \n "))
    if time <= 0:
        print(ValueError)

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year(s): ${total:.2f}")