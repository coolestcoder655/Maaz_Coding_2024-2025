import matplotlib.pyplot as plt

_, ax = plt.subplots()

apps = ['WhatsApp', 'Instagram', 'TikTok', 'Snapchat', 'YouTube']
votes = [18, 22, 15, 10, 25]

def generateColors(listOfX: list) -> list:
    color = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    colors = list()
    index = 0
    for x in range(1, len(listOfX) + 1):
        index += 1
        if index > (len(color) - 1):
            index = 0
        
        colors.append(color[index])

    return colors


explodeValues = [0, 0, 0, 0, 0.2]

cc = plt.Circle((0, 0), radius=0.7, fc="white")
plt.pie(votes, labels=apps, normalize=True, autopct="%1.1f%%", shadow=True, colors=generateColors(votes), startangle=90, explode=explodeValues)
plt.gca().add_artist(cc)
plt.axis("equal")
plt.title(r"$\it{Favorite}$ $\it{App}$ $\it{Pole}$ $\it{Results}$ - $\bf{Percent}$")
plt.show()