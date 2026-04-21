# Last updated: 4/21/2026, 8:42:39 AM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k=len(nums)
        s=set(nums)
        for i in range(1,k+2):
            if i not in s:
                return i
        return 1
         
        