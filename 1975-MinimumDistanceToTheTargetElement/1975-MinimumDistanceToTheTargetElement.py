# Last updated: 4/20/2026, 1:25:41 PM
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        k=[abs(i-start) for i in range(len(nums)) if nums[i]==target]
        return min(k)        
        