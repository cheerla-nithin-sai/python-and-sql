# Last updated: 4/20/2026, 1:25:24 PM
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = []
        for i in range(len(nums)):
            curr=nums[i][i]
            l.append("1" if curr=='0' else '0')
        return "".join(l)