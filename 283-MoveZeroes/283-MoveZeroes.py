# Last updated: 4/21/2026, 8:41:13 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp = [0]*n
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp[k]=nums[i]
                k+=1
        for i in range(len(nums)):
            nums[i]=temp[i]

        return nums