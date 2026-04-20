# Last updated: 4/20/2026, 1:25:21 PM
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        l=0
        nums.sort()
        n=len(nums)
        m=float('inf')
        while l+k<=n:
            m=min(nums[l+k-1]-nums[l],m)
            l+=1
        return m

