from words import easyWords, mediumWords, hardWords
from bigVariables import hangMans
from utilties import clearOutput
from typing import Union
from time import sleep

# Functions
def getHangman(tries) -> Union[None, str]:          # Returns The Respective Hangman For How Many Tries  {}
    global keyboard
    global crossedOutLetters
    global letters
    global correctLetters
    global debug

    for key in list(hangMans.keys()):
        if key == tries:
            return hangMans.get(key)
    return None
        
def getRandomWord(difficulty: str) -> Union[None, str]:     # Gets A Random Word Based On The Difficulty  {}
    from random import choice as ranChoice
    global keyboard
    global crossedOutLetters
    global letters
    global correctLetters
    global debug

    difficulty = difficulty.lower()
    try:
        match difficulty:
            case "easy":
                return ranChoice(easyWords)
            case "medium":
                return ranChoice(mediumWords)
            case "hard":
                return ranChoice(hardWords)
            case _:
                raise ValueError()
    except ValueError as v:
        print(f"An Error Occured: {v} \n Please Contact Developer. Error Code: F1-01")
        return None

def crossOutLetter(crossedOut: str) -> None:                #                                              {}
    global keyboard
    global crossedOutLetters
    global letters
    global correctLetters
    global debug

    if len(crossedOut) != 1:
        print(f"An Error Occured. \n Please Contact Developer. Error Code: F2-01")
        print(len(crossedOut))
        return None
    
    try:
        keyboard = keyboard.replace(crossedOut, crossedOutLetters.get(crossedOut, None))
    except TypeError as t:
        print(f"An Error Occured: {t} Please Contact Developer. Error Code F2-02")
    return None

def getHint():
    global keyboard
    global crossedOutLetters
    global letters
    global correctLetters
    global debug
    
    index = letters.find("_")
    if index != -1:
        letters = letters[:index] + correctLetters[index] + letters[index + 1:]
    return letters

def replaceAtIndex(s: str, index: int, replacement: str) -> str:
    return s[:index] + replacement + s[index + 1:]

def revealLetter(crossedOut):
    global keyboard
    global crossedOutLetters
    global letters
    global correctLetters
    global debug

    index = correctLetters.find(crossedOut)
    return replaceAtIndex(letters, index, crossedOut)

# Variables

global keyboard
global crossedOutLetters
global letters
global correctLetters
global debug
tries = 1

keyboard = """
    q w e r t y u i o p
     a s d f g h j k l
       z x c v b n m
"""

crossedOutLetters = {
    "q": "̶q̶", "w": "̶w̶", "e": "̶e̶", "r": "̶r̶", "t": "̶t̶", "y": "̶y̶", "u": "̶u̶", "i": "̶i̶", "o": "̶o̶", "p": "̶p̶",
    "a": "̶a̶", "s": "̶s̶", "d": "̶d̶", "f": "̶f̶", "g": "̶g̶", "h": "̶h̶", "j": "̶j̶", "k": "̶k̶", "l": "̶l̶",
    "z": "̶z̶", "x": "̶x̶", "c": "̶c̶", "v": "̶v̶", "b": "̶b̶", "n": "̶n̶", "m": "̶m̶"
}

debug = True

clearOutput()
print("Welcome to Digital Hangman!!!")

# Initalization

while True:
    userDifficulty = (input("Please Enter Your Difficulty: \n Walk In The Park: Easy \n Life. : Medium \n Hell On Earth: Hard \n ")).lower()
    if userDifficulty != "easy" and userDifficulty != "medium" and userDifficulty != "hard":
        if userDifficulty == "walk in the park":
            userDifficulty = "easy"
            break
        elif userDifficulty == "life." or userDifficulty == "life":
            userDifficulty = "medium"
            break
        elif userDifficulty == "hell on earth":
            userDifficulty = "hard"
            break
        else:
            print("Invalid Difficulty Has Been Selected. Please Try Again.")
    else:
        break

correctLetters = getRandomWord(userDifficulty)

if userDifficulty == "easy":
    letters = "____"
    hintsLeft = 3
elif userDifficulty == "medium":
    letters = "______"
    hintsLeft = 2
elif userDifficulty == "hard":
    letters = "________"
    hintsLeft = 1
else:
    print("An Error Occured. Please Contact The Developer.")

# Actual Code

clearOutput()

print("Can Quit Game. (Control + C)")

while True:

    if debug:
        print(f"Correct Word: {correctLetters}")

    try:
        if tries == 6:
            print("Lost. The Correct Word Was...")
            sleep(1.5)
            print(correctLetters)
            break
        elif letters == correctLetters:
            print("You Won!!! Good Job!!!")
            break
        print(getHangman(tries))
        print(keyboard)
        print(letters, end="\n \n")
        letterChoice = input("Please Enter Your Choice of Letter:")
        clearOutput()
        if letterChoice not in correctLetters:
            tries += 1
            print("WRONG!!")
            crossOutLetter(letterChoice)
        elif letterChoice in correctLetters:
            print("CORRECT!!!")
            crossOutLetter(letterChoice)
            letters = revealLetter()
        elif letterChoice == "hint":
            if hintsLeft >= 0:
                print("No Hints Left.")
            letters = getHint()
                
    except KeyboardInterrupt:
        print("\n Exiting Game...")
        break
    except Exception:
        pass

input()