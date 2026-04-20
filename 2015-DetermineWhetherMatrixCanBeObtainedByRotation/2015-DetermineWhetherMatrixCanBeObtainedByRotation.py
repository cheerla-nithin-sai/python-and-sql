# Last updated: 4/20/2026, 1:25:37 PM
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if mat==target:
                return True
            mat=[list(r) for r in zip(*mat[::-1])]
            
        return False
        