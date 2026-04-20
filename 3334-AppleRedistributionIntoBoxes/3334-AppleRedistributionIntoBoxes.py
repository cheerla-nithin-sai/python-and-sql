# Last updated: 4/20/2026, 1:24:36 PM
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        t=sum(apple)
        if t>sum(capacity):
            return -1
        elif t==sum(capacity):
            return len(capacity)
        min_box=0
        capacity=sorted(capacity,reverse=True)
        while t>0:
            t-=capacity[min_box]
            min_box+=1
        return min_box

        