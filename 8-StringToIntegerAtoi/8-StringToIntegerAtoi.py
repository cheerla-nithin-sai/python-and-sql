# Last updated: 4/21/2026, 8:42:56 AM
class Solution:
    def myAtoi(self, s: str) -> int:
        ans=""
        l=[]
        for i in range(len(s)):
            if s[i]==" " and len(ans)==0:
                continue
            if s[i]!=" " and (s[i] in '-+' or s[i].isnumeric()) and len(ans)==0:
                ans+=s[i]
            elif s[i].isnumeric():
                ans+=s[i]
            else:
                break
        if ans=="" or ans in '-+':
            return 0
        else:
            if int(ans)<-(2**31):
                return -(2**31)
            elif int(ans)>(2**31-1):
                return (2**31-1)
            else:
                return int(ans)
        