# Question: Given a list of temperatures in Celsius:
# Write a Python function that:
# Converts all temperatures to Fahrenheit.
# Removes any temperatures below 68°F (20°C).
# Returns the updated list of temperatures in Fahrenheit.

temperatures = [22, 25, 20, 18, 30, 26, 23]
newTemperatures = []

for x in temperatures:
    y = (x * 9/5) + 32
    newTemperatures.append(y)
for z in newTemperatures:
    if z < 68:
        newTemperatures.pop(newTemperatures.index(z))

print(f"New Temperatures: {newTemperatures}")