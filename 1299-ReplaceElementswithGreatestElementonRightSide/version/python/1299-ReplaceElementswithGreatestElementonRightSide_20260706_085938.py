# Last updated: 7/6/2026, 8:59:38 AM
1class Solution:
2    def replaceElements(self, arr: List[int]) -> List[int]:
3        # for i in range(len(arr)-1):
4        #     arr[i]=max(arr[i+1:])
5        # arr[-1]=-1
6        # return 
7        m=-1
8        for i in range(len(arr)-1,-1,-1):
9            t=arr[i]
10            arr[i]=m
11            if t>m:
12                m=t
13        return arr