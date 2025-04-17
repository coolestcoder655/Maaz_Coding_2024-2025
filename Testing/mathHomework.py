from math import sqrt


def sortList(*args) -> None:
    lst = [*args]

    """Sorts a list in ascending order."""
    print(sorted(lst))

sortList(-abs(-sqrt(58)), -sqrt(42), -5.3, -8.3, -5 + -8/9, -97/100)