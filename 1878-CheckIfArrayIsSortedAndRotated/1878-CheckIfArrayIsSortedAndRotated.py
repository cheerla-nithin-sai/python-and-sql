# Last updated: 4/20/2026, 1:25:51 PM
class Solution:
    def check(self, nums: List[int]) -> bool:
        idx=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                idx=i
                break
        l = nums[idx:]+nums[:idx]
        return l==sorted(nums)
        