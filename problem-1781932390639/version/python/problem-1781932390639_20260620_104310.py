# Last updated: 6/20/2026, 10:43:10 AM
1class Solution:
2    def checkGoodInteger(self, n: int) -> bool:
3        l=[int(i) for i in list(str(n))]
4        k=[int(i)*int(i) for i in l]
5        return sum(k)-sum(l)>=50