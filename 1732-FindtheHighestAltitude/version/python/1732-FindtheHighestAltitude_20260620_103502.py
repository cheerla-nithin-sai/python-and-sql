# Last updated: 6/20/2026, 10:35:02 AM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        a=0
4        l=[0]
5        for i in gain:
6            l.append(i+a)
7            a+=i
8        return max(l)