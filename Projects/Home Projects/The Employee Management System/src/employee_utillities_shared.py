from typing import Optional


totalEmployeeDict = {}

def listItems(List, index: Optional = None):
    i = 0
    if index:
        for x in List:
            i += 1
            print(x[1], end=f" = {i} \n")
    for x in List:
        i += 1
        print(x, end=f" = {i} \n")