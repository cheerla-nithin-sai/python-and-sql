# Last updated: 4/21/2026, 8:42:19 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-2,0,-1):
            if nums[i-1]==nums[i] and nums[i]==nums[i+1]:
                nums.pop(i+1)
        return len(nums)
        