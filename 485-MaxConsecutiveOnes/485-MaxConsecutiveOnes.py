# Last updated: 4/21/2026, 8:40:59 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        c=0
        for i in nums:
            if i==1:
                c+=1
            else:
                m=max(m,c)
                c=0
        return max(m,c)

        