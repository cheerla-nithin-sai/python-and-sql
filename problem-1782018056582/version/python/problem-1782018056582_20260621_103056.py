# Last updated: 6/21/2026, 10:30:56 AM
1class Solution:
2    def maxDistance(self, moves: str) -> int:
3        d={}
4        for i in moves:
5            if i in d:
6                d[i]+=1
7            else:
8                d[i]=1
9        return abs(d.get('L',0)-d.get('R',0))+abs(d.get('U',0)-d.get('D',0))+d.get('_',0)
10        
11