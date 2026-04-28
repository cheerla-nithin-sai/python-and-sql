# Last updated: 4/28/2026, 11:29:37 AM
1class Solution:
2    def minOperations(self, grid: List[List[int]], x: int) -> int:
3        a=[]
4        for i in grid:
5            for j in i:
6                a.append(j)
7        a.sort()
8        b=len(a)
9        c=0
10        d=a[b//2]
11        for i in a:
12            if i%x!=d%x:
13                return -1
14            c+=abs(d-i)//x
15        return c