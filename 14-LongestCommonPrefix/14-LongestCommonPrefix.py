# Last updated: 4/21/2026, 8:42:52 AM

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x:len(x))
        res=""
        for i in range(len(strs[0])):
            pre=strs[0][:i+1]
            t=True
            for j in strs:
                if j[:i+1]!=pre:
                    t=False
            if t:
                res=pre
        return res
