# Last updated: 4/20/2026, 1:25:54 PM
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre=0
        max_pre=0
        pre_sum=0
        for i in nums:
            pre_sum+=i
            min_pre=min(min_pre,pre_sum)
            max_pre=max(max_pre,pre_sum)
        return max_pre-min_pre
        