# Last updated: 7/15/2026, 10:05:43 AM
1class Solution:
2    def gcdOfOddEvenSums(self, n: int) -> int:
3        a,b=0,0
4        for i in range(1,2*n+1):
5            if i%2==0:
6                a+=i
7            else:
8                b+=i
9        def gcd_iterative(a, b):
10            while b != 0:
11                a, b = b, a % b
12            return a
13        return gcd_iterative(a,b)