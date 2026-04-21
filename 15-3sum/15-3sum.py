# Last updated: 4/21/2026, 8:42:51 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        s=set()
        nums.sort()
        for i in range(len(nums)-2):
            l=i+1
            r=n-1
            while l<r:
                ss=nums[i]+nums[l]+nums[r]
                if ss<0:
                    l+=1
                elif ss>0:
                    r-=1
                else:
                    s.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
        res=list(s)
        return res
        