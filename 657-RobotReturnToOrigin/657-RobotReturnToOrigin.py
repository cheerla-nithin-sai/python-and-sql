# Last updated: 4/20/2026, 1:28:14 PM
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        s=0
        l=0
        for i in moves:
            if i=='U':
                s+=1
            elif i=='D':
                s-=1
            elif i=='L':
                l+=1
            else:
                l-=1
        return s==l==0
        