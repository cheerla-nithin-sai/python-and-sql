# Last updated: 4/24/2026, 5:48:35 PM
1class Solution:
2    def furthestDistanceFromOrigin(self, moves: str) -> int:
3        l,r,u=0,0,0
4        for i in moves:
5            if i=='L':
6                l+=1
7            elif i=='R':
8                r+=1
9            else:
10                u+=1
11        return abs(l-r)+u
12        