# Last updated: 4/20/2026, 1:26:03 PM
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c =0
        l=0
        r=len(nums)-1
        nums.sort()
        while l<r:
            if nums[l]+nums[r]==k:
                c+=1
                l+=1
                r-=1
            elif (nums[l]+nums[r])<k:
                l+=1
            else:
                r-=1
        return c