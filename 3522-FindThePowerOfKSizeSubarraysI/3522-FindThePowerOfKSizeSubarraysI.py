# Last updated: 4/20/2026, 1:24:28 PM
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if k==1 or n==1:
            return nums
        l = [-1]*(n-k+1)
        cons_num=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                cons_num+=1
            else:
                cons_num=1
            if cons_num>=k:
                l[i-k+1]=nums[i]
        return l

        return l

        