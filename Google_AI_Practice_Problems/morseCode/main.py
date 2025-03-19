class Solution:
    morseCode = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
        "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
    }
    def translateMorse(string: str) -> str:
        translated = ""
        string = list((string.lower()))
        for letter in string:
            translated = translated + Solution.morseCode[letter]
        return translated

print(Solution.translateMorse("SOS"))