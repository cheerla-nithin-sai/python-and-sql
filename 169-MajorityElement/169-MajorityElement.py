# Last updated: 4/21/2026, 8:41:55 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        if len(nums)==1:
            return nums[0]
        k=len(nums)//2
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return max([i for i,j in d.items() if j>k])

