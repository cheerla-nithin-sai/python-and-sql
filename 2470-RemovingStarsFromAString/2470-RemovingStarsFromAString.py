# Last updated: 4/20/2026, 1:25:09 PM
class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for i in s:
            if i!='*':
                l.append(i)
            else:
                l.pop()
        return ''.join(l)
            
        