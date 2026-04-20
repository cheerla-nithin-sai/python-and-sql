# Last updated: 4/20/2026, 1:28:16 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c = sum(nums[:k])
        s = c
        for i in range(len(nums)-k):
            c = c-nums[i]+nums[i+k]
            s=max(c,s)
        return s/k