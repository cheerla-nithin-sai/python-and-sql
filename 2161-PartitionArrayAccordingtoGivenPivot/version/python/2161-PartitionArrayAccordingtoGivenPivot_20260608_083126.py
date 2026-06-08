# Last updated: 6/8/2026, 8:31:26 AM
1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        l=[]
4        r=[]
5        p=[]
6        for i in nums:
7            if i < pivot:
8                l.append(i)
9            elif i>pivot:
10                r.append(i)
11            else:
12                p.append(i)
13        return l+p+r
14