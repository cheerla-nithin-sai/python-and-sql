# Last updated: 4/20/2026, 1:24:04 PM
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        r=0
        a=n
        for i in range(n):
            while r<n and nums[r]<=nums[i]*k:
                r+=1
            a=min(a,n-(r-i))
        return a
        

        