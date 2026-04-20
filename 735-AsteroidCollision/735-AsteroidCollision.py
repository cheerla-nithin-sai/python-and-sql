# Last updated: 4/20/2026, 1:28:06 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l = []
        for i in asteroids:
            l.append(i)
            while len(l)>1 and l[-1]<0 and l[-2]>0:
                last = l.pop()
                prev =l.pop()
                if abs(last)>prev:
                    l.append(last)
                elif abs(last)<prev:
                    l.append(prev)
        return l

            
