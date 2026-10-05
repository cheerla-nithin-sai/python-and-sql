# Last updated: 10/5/2026, 10:06:49 PM
1class Solution:
2    def scoreOfParentheses(self, s: str) -> int:
3        l=[0]
4        for i in s:
5            if i=='(':
6                l.append(0)
7            else:
8                c=l.pop()
9                l[-1]+=max(1,2*c)
10        return l[0]