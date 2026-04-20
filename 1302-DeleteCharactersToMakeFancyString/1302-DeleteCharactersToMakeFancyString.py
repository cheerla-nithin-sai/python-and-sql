# Last updated: 4/20/2026, 1:27:23 PM
class Solution:
    def makeFancyString(self, s: str) -> str:
        res=""
        for i in s:
            if len(res)>=2 and res[-1]==i and res[-2]==i:
                continue
            res=res+i
        return res

        