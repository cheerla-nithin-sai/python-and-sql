# Last updated: 4/20/2026, 1:25:47 PM
class Solution:
    def beautySum(self, s: str) -> int:
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if len(s[i:j])>1:
                    l.append(s[i:j])
        c=0
        for i in l:
            d={}
            for j in i:
                if j not in d:
                    d[j]=1
                else:
                    d[j]+=1
            d=sorted(d.items(),key=lambda x:x[1])
            c+=d[-1][1]-d[0][1]
        return c
        