# Last updated: 4/20/2026, 1:24:29 PM
class Solution:
    def minimumLength(self, s: str) -> int:
        c=0
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in d.values():
            if j%2==1:
                c+=j-1
            else:
                c+=j-2
        return len(s)-c

        