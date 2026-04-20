# Last updated: 4/20/2026, 1:24:01 PM
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        i=x
        j=x+k-1
        while i<j:
            for l in range(y,y+k):
                grid[i][l],grid[j][l]=grid[j][l],grid[i][l]
            i,j=i+1,j-1
        return grid       