# Last updated: 4/20/2026, 1:24:41 PM
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        n=n**2
        l=[]
        for i in grid:
            l.extend(i)
        a=sum(l)-sum(set(l))
        b=(n*(n+1))/2-sum(set(l))
        return [a,int(b)]