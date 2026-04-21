# Last updated: 4/21/2026, 8:42:42 AM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=0
        h=len(nums)-1
        while s<=h:
            m=(s+h)//2
            if nums[m]==target:
                s=m
                h=m
                while s>0 and nums[s-1]==target:
                    s-=1
                while h<len(nums)-1 and nums[h+1]==target:
                    h+=1
                return [s,h]
            elif nums[m]>target:
                h=m-1
            else:
                s=m+1
        return [-1,-1]