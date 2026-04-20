# Last updated: 4/20/2026, 1:27:12 PM
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        c=0
        for i in range(len(points)-1):
            x,y=points[i]
            x1,y1=points[i+1]
            c+=max(abs(x1-x),abs(y1-y))
        return c
        