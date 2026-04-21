# Last updated: 4/21/2026, 8:42:21 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(len(nums)):
            for i in range(1,len(nums)):
                if nums[i-1]>nums[i]:
                    nums[i-1],nums[i]=nums[i],nums[i-1]
        return nums
        