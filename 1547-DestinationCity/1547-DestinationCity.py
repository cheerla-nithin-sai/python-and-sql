# Last updated: 4/20/2026, 1:26:22 PM
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()

        for i,j in paths:
            start.add(i)
            end.add(j)
        return (end-start).pop()
            
        