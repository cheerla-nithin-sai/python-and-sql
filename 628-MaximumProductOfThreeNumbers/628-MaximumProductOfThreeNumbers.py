# Last updated: 4/20/2026, 1:28:18 PM
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        nums = sorted(nums)
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[2],nums[0]*nums[1]*nums[-1])
        