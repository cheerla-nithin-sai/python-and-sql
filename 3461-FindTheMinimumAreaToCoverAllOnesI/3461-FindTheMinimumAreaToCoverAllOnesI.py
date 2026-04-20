# Last updated: 4/20/2026, 1:24:26 PM
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        minr=r
        maxr=0
        minc=c
        maxc=0
        for row in range(r):
            for col in range(c):
                if grid[row][col]==1:
                    minr=min(row,minr)
                    maxr=max(maxr,row)
                    minc=min(minc,col)
                    maxc=max(col,maxc)
        return (maxr-minr+1)*(maxc-minc+1)

        