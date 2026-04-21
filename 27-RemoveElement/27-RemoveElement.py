# Last updated: 4/21/2026, 8:42:48 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=len([i for i in nums if i!=val])
        for i in range(len(nums)-k):
            nums.remove(val)
            nums.append(val)
        return k