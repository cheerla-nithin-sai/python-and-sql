# Last updated: 7/6/2026, 9:12:24 AM
1class Solution:
2    def isGood(self, nums: List[int]) -> bool:
3        m=max(nums)
4        if sum(nums)==(m*(m+1))//2+m and len(set(nums))==m:
5            return True
6        return False