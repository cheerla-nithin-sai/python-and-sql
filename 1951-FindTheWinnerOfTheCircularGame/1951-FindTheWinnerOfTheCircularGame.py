# Last updated: 4/20/2026, 1:25:42 PM
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [i+1 for i in range(n)]
        c= 0
        while n>1:
            c=(c+(k-1))%n
            l.pop(c)
            n-=1
        return l[-1]

        