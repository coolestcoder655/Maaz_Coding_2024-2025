# Longest Word in a Sentence
# Return the longest word in a given sentence string.

def longestWord(s: str):
    words = s.split(' ')
    max_length = 0
    longest = ""

    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest = word

    return longest