try:
    with open("Normal Classwork\File I and O\learningOccurences\learning.txt") as file:
        data = file.read()

    data = data.split(" ")

    index = data.index("learning")

    print(index + 1)
except ValueError as v:
    print(f"-1 : {v}")