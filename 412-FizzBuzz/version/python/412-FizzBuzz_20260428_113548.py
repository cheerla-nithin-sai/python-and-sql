# Last updated: 4/28/2026, 11:35:48 AM
1class Solution:
2    def fizzBuzz(self, n: int) -> List[str]:
3        l=[]
4        for i in range(1,n+1):
5            if i%3==0 and i%5==0:
6                l.append("FizzBuzz")
7            elif i%3==0:
8                l.append("Fizz")
9            elif i%5==0:
10                l.append("Buzz")
11            else:
12                l.append(str(i))
13        return l