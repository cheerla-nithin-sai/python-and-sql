# Last updated: 4/21/2026, 8:41:31 AM
class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        len_arr=float('inf')
        l,r=0,0
        sum_arr=0
        for i in range(len(nums)):
            sum_arr+=nums[i]
            while sum_arr>=k:
                len_arr=min(len_arr,r-l+1)
                sum_arr-=nums[l]
                l+=1
            r+=1
        if len_arr==float('inf'):
            return 0
        else:
            return len_arr
        