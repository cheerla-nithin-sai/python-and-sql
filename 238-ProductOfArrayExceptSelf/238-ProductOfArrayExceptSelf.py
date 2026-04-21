# Last updated: 4/21/2026, 8:41:21 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre=1
        post=1
        l = [1]*n
        for i in range(n):
            l[i]*=pre
            pre*=nums[i]
            l[n-i-1]*=post
            post*=nums[n-i-1]
        return l
        