from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = False
        x = 1
        for index, _ in enumerate(nums):
            if (nums[index]) + (nums[index + 1]) == target:
                return index, index + 1

nums = [3, 2, 3]

indexs = (Solution.twoSum(Solution, nums, 6))
print(nums[indexs[0]])
print(nums[indexs[1]])

print(nums[indexs[0]] + nums[indexs[1]])