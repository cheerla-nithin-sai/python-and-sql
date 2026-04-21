# Last updated: 4/21/2026, 8:41:39 AM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k!=0:
            nums[:k],nums[k:] = nums[-k:],nums[:-k]

        