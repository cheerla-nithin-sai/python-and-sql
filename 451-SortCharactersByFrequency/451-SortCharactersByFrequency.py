# Last updated: 4/21/2026, 8:41:00 AM
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=sorted(d.items(),key=lambda x:x[1],reverse=True)
        k=""
        for i in l:
            j=i[1]
            while j!=0:
                k+=i[0]
                j-=1        
        return k