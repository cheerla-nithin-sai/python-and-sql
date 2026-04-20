# Last updated: 4/20/2026, 1:28:17 PM
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c))
        i=0
        if n*n==c:
            return True
        while i<=n:
            k = i*i+n*n
            if k==c:
                return True
            elif k>c:
                n-=1
            elif k<c:
                i+=1
        return False

        