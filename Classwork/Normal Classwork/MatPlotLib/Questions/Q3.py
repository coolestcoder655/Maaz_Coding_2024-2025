# You measured your height (in cm) and your shoe size over 5 years. Plot to see if there’s a pattern.

import matplotlib.pyplot as plt
import random


heights = [120, 125, 130, 135, 140]
shoe_sizes = [3, 4, 5, 6, 7]

sizes = [100, 200, 50, 80, 1232]

colors = ["red", "orange", "yellow", "green", "blue"]

plt.scatter(heights, shoe_sizes, color=colors, s=sizes, marker="*")
plt.title("Heights vs Shoe Sizes")
plt.xlabel("Heights")
plt.ylabel("Shoe Sizes")
plt.show()