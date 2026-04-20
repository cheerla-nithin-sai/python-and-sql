# Last updated: 4/20/2026, 1:27:44 PM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        bal=0
        l=[]
        for i in s:
            if i=="(":
                if bal>0:
                    l.append(i)
                bal+=1
            else:
                if bal>1:
                    l.append(i)
                bal-=1
        return "".join(l)