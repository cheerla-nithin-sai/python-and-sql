# Last updated: 4/21/2026, 8:42:24 AM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        rows=[0]*n
        cols=[0]*m
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]==0:
                    rows[row]=1
                    cols[col]=1
        for i in range(n):
            for j in range(m):
                if rows[i]==1 or cols[j]==1:
                    matrix[i][j]=0
        return matrix