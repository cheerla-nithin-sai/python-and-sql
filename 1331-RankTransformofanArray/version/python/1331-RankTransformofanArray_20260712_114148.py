# Last updated: 7/12/2026, 11:41:48 AM
1class Solution:
2    def arrayRankTransform(self, arr: List[int]) -> List[int]:
3        d={}
4        j=1
5        for i in sorted(set(arr)):
6            d[i]=j
7            j+=1
8        return [d[i] for i in arr]