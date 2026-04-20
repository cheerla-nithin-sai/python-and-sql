# Last updated: 4/20/2026, 1:27:52 PM
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        for row in range(len(matrix)-2,-1,-1):
            for col in range(n):
                min_below=matrix[row+1][col]
                if col>0:
                    min_below=min(min_below,matrix[row+1][col-1])
                if col<n-1:
                    min_below=min(min_below,matrix[row+1][col+1])
                matrix[row][col]+=min_below
        return min(matrix[0])
        