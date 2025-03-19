class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reversedX = (str(x)[::-1])
        return x == reversedX