class Solution:
    def sum(numbers: str) -> int:
        sum = list(numbers)
        total = 0
        for num in sum:
            num = int(num)
            total += num
        return total
    
print(Solution.sum("123"))