# Last updated: 4/21/2026, 8:41:28 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)
        