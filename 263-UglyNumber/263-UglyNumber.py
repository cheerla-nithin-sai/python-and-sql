# Last updated: 4/21/2026, 8:41:15 AM
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        nums = [2,3,5]
        for i in nums:
            while n%i==0:
                n=n//i
        return n==1