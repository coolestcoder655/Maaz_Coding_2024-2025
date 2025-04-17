from math import sqrt

def squareRoots(n):
    """Returns a list of square roots of numbers from 1 to n."""
    return [sqrt(i) for i in range(1, n + 1)]


squareRoots(16)