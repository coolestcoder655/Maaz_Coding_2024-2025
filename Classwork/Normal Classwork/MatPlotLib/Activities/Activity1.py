import matplotlib.pyplot as plt


_, ax = plt.subplots()
monthsLettters = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
months = list(range(1, len(monthsLettters) + 1))
groceries = [120, 135, 110, 140, 130, 125]
entertainment = [60, 75, 70, 90, 85, 100]

ax.bar(months, groceries, 0.5, label="Groceries")
ax.bar(months, entertainment, 0.5, label="Entertainment")
ax.set_facecolor("red")
ax.legend()
ax.set_xlabel(r'$\bf{Time}$ - $\it{(Months)}$', fontsize=16)
ax.set_ylabel(r'$\bf{Cost}$ - $\it{(Dollars)}$', fontsize=16)
ax.set_title(f"Cost of Groceries and Entertainment over {len(monthsLettters)} Months")
ax.grid(True)
ax.set_xticks(months, monthsLettters)

plt.show()