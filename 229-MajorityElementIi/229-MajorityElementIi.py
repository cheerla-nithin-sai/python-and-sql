# Last updated: 4/21/2026, 8:41:23 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return [i for i,j in d.items() if j>n//3]
        