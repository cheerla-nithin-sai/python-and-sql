# Last updated: 4/20/2026, 1:27:54 PM
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        k=0
        for i in s:
            if i=="(":
                count+=1
            else:
                if count>0:
                    count-=1
                else:
                    k+=1
        return max(k,count+k)



        