# Last updated: 4/21/2026, 8:39:23 AM
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in grid:
            c+=len([j for j in i if j<0])
        return c


        