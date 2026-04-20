# Last updated: 4/20/2026, 1:25:32 PM
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n==1:
            return 5
        modu=10**9+7
        res=0
        if n%2==0:
            res=pow(5,n//2,modu)*pow(4,n//2,modu)
        else:
            res=pow(5,n//2+1,modu)*pow(4,n//2,modu)
        return res%modu