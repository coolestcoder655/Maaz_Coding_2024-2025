# Count Vowels in a String
# Write a function that takes a string and returns the number of vowels in it.

def count_vowels(s: str):
    s = s.lower()
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
    totalCount: int = 0

    for vowel in vowels:
        vowelsInWord = s.count(vowel)
        totalCount += vowelsInWord
        print(f'{vowel.capitalize()}: {vowelsInWord}')

    print(f'Total Count: {totalCount}')