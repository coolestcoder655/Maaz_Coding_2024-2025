# WAP that takes a sentence and a word as input, then counts how many times that word appears in the sentence.

sentence = input("Welcome to the Word Counter \n Please enter the sentence with the word to be checked:")
word = input("Please enter the word to be checked in the sentence.:")

sentence = sentence.lower()
word = word.lower()

occurrences = sentence.count(word)

if sentence and word != "":
    print(occurrences)
else:
    print("The word/sentence cannot be used for checking due to the lack of words inside either of the text boxes.")

# Use Lists & .split() functions.