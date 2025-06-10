# You spend 24 hours in a day like this: 8 hours sleeping, 6 hours at school, 2 hours doing homework, and 8 hours free time. Show this in a pie chart.
import matplotlib.pyplot as plt

activies = {
    "sleeping": 8,
    "school": 6,
    "homework": 2,
    "free time": 8
}

colors = ["red", "yellow", "green", "blue"]

cc = plt.Circle((0, 0), radius=0.02, fc="white")

plt.pie(activies.values(), labels=list(activies.keys()), normalize=True, autopct="%1.1f%%", shadow=True, colors=colors, startangle=90)
plt.gca().add_artist(cc)
plt.axis("equal")
plt.title("Activies in a day")
plt.show()