# Last updated: 4/25/2026, 10:37:49 AM
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l,r,u=0,0,0
        for i in moves:
            if i=='L':
                l+=1
            elif i=='R':
                r+=1
            else:
                u+=1
        return abs(l-r)+u
        