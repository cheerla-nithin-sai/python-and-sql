# Last updated: 4/20/2026, 1:27:57 PM
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursrequired(l,k):
            totalh=0
            for i in range(len(l)):
                totalh+=math.ceil(l[i]/k)
            return totalh
        l=1
        r=max(piles)
        while l<=r:
            m=(l+r)//2
            H=hoursrequired(piles,m)
            if H<=h:
                r=m-1
            else:
                l=m+1
        return l