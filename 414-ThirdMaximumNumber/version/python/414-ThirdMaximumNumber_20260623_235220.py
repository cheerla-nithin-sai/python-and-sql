# Last updated: 6/23/2026, 11:52:20 PM
1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3        if len(set(nums))<3:
4            return max(nums)
5        k=sorted(list(set(nums)))
6        return k[-3]