# Last updated: 4/21/2026, 8:41:51 AM
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count =0
        while n>0:
            n=n//5
            count+=n
        return count
        