# Your school conducted a survey to find out how many students like different fruits. Plot the data using a bar chart.
import matplotlib.pyplot as plt
import numpy as np


barColors = ["red", "yellow", "orange", "green", "purple"]

students = [120, 240, 456, 942, 345]
fruits = ["apples", "bananas", "oranges", "watermelon", "grapefruit"]

_, ax = plt.subplots()
ax.bar(fruits, students, color=barColors, label="fruits")
ax.set_xlabel("Fruits")
ax.set_ylabel("Students")
ax.set_title("Fruits vs. Students")
ax.grid(True)
ax.legend()

plt.show()