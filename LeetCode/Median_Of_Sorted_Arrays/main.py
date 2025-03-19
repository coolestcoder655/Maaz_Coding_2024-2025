class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums2.extend(nums1)
        isEven = lambda x: x % 2 == 0
        if isEven(len(nums2)):
            return (nums2[len(nums2) // 2] + nums2[(len(nums2) // 2) - 1]) / 2
        else:
            return nums2[len(nums2) // 2]