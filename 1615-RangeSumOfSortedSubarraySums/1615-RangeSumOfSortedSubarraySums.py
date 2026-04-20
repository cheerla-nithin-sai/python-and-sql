# Last updated: 4/20/2026, 1:26:18 PM
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l = []
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                l.append(s)
        l.sort()
        c=0
        m=10**9+7
        for i in range(left-1,right):
            c=(c+l[i])%m
        return c
        
        
                
        