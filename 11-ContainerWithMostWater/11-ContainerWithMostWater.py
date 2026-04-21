# Last updated: 4/21/2026, 8:42:54 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,a=0,len(height)-1,0
        while l<r:
            a =max(a,(r-l)*min(height[r],height[l]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return a
        