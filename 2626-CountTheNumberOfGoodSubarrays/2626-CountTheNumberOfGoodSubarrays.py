# Last updated: 4/20/2026, 1:24:57 PM
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        c=0
        n=len(nums)
        pairs=0
        d=defaultdict(int)
        l=0
        for r,num in enumerate(nums):
            pairs+=d[num]
            d[num]+=1
            while pairs>=k:
                c+=n-r
                d[nums[l]]-=1
                pairs-=d[nums[l]]
                l+=1
        return c
        