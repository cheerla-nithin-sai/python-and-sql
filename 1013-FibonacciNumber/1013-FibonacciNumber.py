# Last updated: 4/20/2026, 1:27:50 PM
class Solution:
    def fib(self, n: int) -> int:
        def febn(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            else:
                return febn(n-1)+febn(n-2)
        return febn(n)
        