class Solution:
    vowels = ["a", "e", "i", "o", "u"]
    def countVowels(self, input: str) -> int:
        count = 0
        input = input.lower()
        for vowel in Solution.vowels:
            count += input.count(vowel)
        return count
    

solution = Solution()
print(solution.countVowels("hello"))