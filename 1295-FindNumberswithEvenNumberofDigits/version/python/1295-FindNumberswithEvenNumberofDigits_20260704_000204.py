# Last updated: 7/4/2026, 12:02:04 AM
1class Solution:
2    def findNumbers(self, nums: List[int]) -> int:
3        return len([i for i in nums if len(str(i))%2==0])