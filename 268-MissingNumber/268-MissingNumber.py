# Last updated: 4/21/2026, 8:41:14 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return n*(n+1)//2-sum(nums)
        