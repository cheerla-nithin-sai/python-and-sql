# Last updated: 4/20/2026, 1:25:15 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low=[]
        eq=[]
        high=[]
        for i in nums:
            if i<pivot:
                low.append(i)
            elif i==pivot:
                eq.append(i)
            else:
                high.append(i)
        return low+eq+high
        