# Last updated: 4/20/2026, 1:28:11 PM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in operations:
            try:
                l.append(int(i))
            except:
                pass
            if i=='C':
                l.pop()
            elif i=='D':
                l.append(l[-1]*2)
            elif i=='+':
                l.append(l[-1]+l[-2])
        return sum(l)