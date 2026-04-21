# Last updated: 4/21/2026, 8:42:17 AM
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return True
            elif nums[l]==nums[m]==nums[r]:
                l+=1
                r-=1
                continue
            elif nums[m]>=nums[l]:
                if target>=nums[l] and target<=nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if target>=nums[m] and target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return False
        