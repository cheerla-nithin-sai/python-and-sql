# Last updated: 6/21/2026, 12:15:51 AM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> List[int]:
3        s=set()
4        for i in nums:
5            if i not in s:
6                s.add(i)
7            else:
8                s.remove(i)
9        return list(s)