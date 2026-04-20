# Last updated: 4/20/2026, 1:25:17 PM
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        m=0
        for i in range(n-1,-1,-1):
            if colors[i]!=colors[0]:
                m=max(m,i)
                break
        for i in range(n):
            if colors[i]!=colors[n-1]:
                m=max(m,n-i-1)
                break
        return m
