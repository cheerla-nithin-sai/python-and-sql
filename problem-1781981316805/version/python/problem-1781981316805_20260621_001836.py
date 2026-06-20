# Last updated: 6/21/2026, 12:18:36 AM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        s=set()
4        for i in nums:
5            if i not in s:
6                s.add(i)
7            else:
8                return i