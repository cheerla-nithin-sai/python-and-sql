# Last updated: 4/20/2026, 1:26:11 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        m=0
        l=0
        for i in s:
            print(l)
            if i=="(":
                m+=1
            elif i==")":
                m-=1
            l=max(m,l)
        return l

        