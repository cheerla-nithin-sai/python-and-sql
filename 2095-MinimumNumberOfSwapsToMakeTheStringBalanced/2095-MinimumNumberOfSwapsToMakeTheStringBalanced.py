# Last updated: 4/20/2026, 1:25:25 PM
class Solution:
    def minSwaps(self, s: str) -> int:
        k=0
        for i in s:
            if i=="[":
                k+=1
            else:
                if k>0:
                    k-=1
        return (k+1)//2
        