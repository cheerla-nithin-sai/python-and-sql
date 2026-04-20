# Last updated: 4/20/2026, 1:25:50 PM
class Solution:
    def minOperations(self, s: str) -> int:
        c=0
        d=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=='1':
                    c+=1
                if s[i]=='0':
                    d+=1
            else:
                if s[i]=='0':
                    c+=1
                if s[i]=='1':
                    d+=1
        return min(d,c)
        