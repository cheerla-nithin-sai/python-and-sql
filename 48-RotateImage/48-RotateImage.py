# Last updated: 4/21/2026, 8:42:38 AM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        for row in range(n):
            for col in range(row):
                matrix[col][row],matrix[row][col]=matrix[row][col],matrix[col][row]
        for i in range(n):
            matrix[i].reverse()
        return matrix

        