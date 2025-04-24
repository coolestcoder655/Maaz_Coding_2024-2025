global letters
letters = "____"

def giveHint(letters):
    correctLetters = "Lake"
    index = letters.find("_")
    if index != -1:
        letters = letters[:index] + correctLetters[index] + letters[index + 1:]
    return letters

print(letters)

input()
letters = giveHint(letters)
print(letters)

letters = "L_k_"

input()
letters = giveHint(letters)
print(letters)

input()
letters = giveHint(letters)
print(letters)