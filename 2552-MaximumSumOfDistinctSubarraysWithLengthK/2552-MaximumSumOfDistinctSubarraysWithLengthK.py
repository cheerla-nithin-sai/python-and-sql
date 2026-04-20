# Last updated: 4/20/2026, 1:25:05 PM
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        end=0
        n=len(nums)
        s=set()
        winsum=0
        maxsum=0
        for start in range(n):
            while end<n and end-start<k and nums[end] not in s:
                winsum+=nums[end]
                s.add(nums[end])
                end+=1
            if end-start==k:
                maxsum=max(maxsum,winsum)
            s.remove(nums[start])
            winsum-=nums[start]
        return maxsum