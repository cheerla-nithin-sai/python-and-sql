# Last updated: 4/21/2026, 8:40:55 AM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ele=0
        for i in nums:
            ele=ele^i
        return ele