# Last updated: 4/21/2026, 8:41:30 AM
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=3:
            return max(nums)
        def maxrob(nums):
            dp=[0]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return max(dp[-1],dp[-2])
        return max(maxrob(nums[1:]),maxrob(nums[:-1]))
        