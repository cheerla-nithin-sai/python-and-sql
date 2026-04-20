# Last updated: 4/20/2026, 1:27:09 PM
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        l=[]
        for i in range(1,n):
            b=n-i
            if "0" not in str(i)+str(b):
                l.append(i)
                l.append(b)
                break
        return l
            
        