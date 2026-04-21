# Last updated: 4/21/2026, 8:42:00 AM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r =0,len(nums)-1
        c = float("inf")
        while l<r:
            m=l+(r-l)//2
            c = min(c,nums[m])
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m-1
        return min(c,nums[l])