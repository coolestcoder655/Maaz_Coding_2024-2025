import matplotlib.pyplot as plt


students = ['Ali', 'Sara', 'Bilal', 'Ayesha', 'Hamza', 'Zara', 'Usman',
'Fatima', 'Ahmed', 'Noor']
hours = [2, 4, 3, 5, 1, 6, 4, 7, 2, 5]
marks = [55, 68, 60, 75, 45, 82, 66, 90, 50, 78]
sizes = [mark * 0.5 for mark in marks]

def generateColors(listOfX: list) -> list:
    color = ["r", "y", "g", "c", "b", "m"]
    colors = list()
    index = 0
    for x in range(1, len(listOfX) + 1):
        index += 1
        if index > (len(color) - 1):
            index = 0
        
        colors.append(color[index])

    return colors




_, ax = plt.subplots()
ax.scatter(x=hours, y=marks, s=sizes, c=generateColors(hours))
ax.set_xticks(hours, students)
ax.grid(True)
ax.set_title("Hours Studied vs. Grade")
ax.set_xlabel(r'$\bf{Time}$ - $\it{(Hours)}$', fontsize=16)
ax.set_ylabel(r'$\bf{Grade}$ - $\it{(Percent/100)}$', fontsize=16)

for index, value in enumerate(marks):
    ax.text(hours[index], value + 1, students[index])

plt.show()