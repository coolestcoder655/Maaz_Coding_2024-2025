class Solution:
    def findMax(myList: list) -> int:
        max = 0
        for number in myList:
            if max < number:
                max = number
        return max
    
print(Solution.findMax([3, 7, 2, 8, 5]))