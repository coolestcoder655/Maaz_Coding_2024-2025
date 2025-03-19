# 8.	Count Word Occurrences:
# Count how many times each word appears in a sentence.

wordCounts = {

}

sentence = "The very tall and very skinny man, with his very long and very flowing very red cape, walked very slowly down the very long and very winding very cobblestone street."


# Using Split Function to Add Every Word Into a List
words = sentence.split()

# Finds all Unique Words and Creates a Set With Them
sentenceSet = set(words)


# Creates a Dictonary Value with the key of the uniqueWord and how many times the word appears as it's value.
for uniqueWord in sentenceSet:
    wordCounts[uniqueWord] = sentence.count(uniqueWord)

print(wordCounts)