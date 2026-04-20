# Last updated: 4/20/2026, 1:24:34 PM
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r,c=len(grid),len(grid[0])
        cnt=0
        for i in range(r):
            for j in range(c):
                if i>0:
                    grid[i][j]+=grid[i-1][j]
                if j>0:
                    grid[i][j]+=grid[i][j-1]
                if i>0 and j>0:
                    grid[i][j]-=grid[i-1][j-1]
                if grid[i][j]<=k:
                    cnt+=1
        return cnt