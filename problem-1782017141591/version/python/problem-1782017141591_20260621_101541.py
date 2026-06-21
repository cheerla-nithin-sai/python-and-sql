# Last updated: 6/21/2026, 10:15:41 AM
1class Solution:
2    def countValidSubarrays(self, nums: list[int], x: int) -> int:
3        n = len(nums)
4        count = 0
5        for l in range(n):
6            s = 0
7            for r in range(l, n):
8                s += nums[r]
9                d = str(s)
10                if int(d[0]) == x and int(d[-1]) == x:
11                    count += 1
12        return count