# Last updated: 4/20/2026, 1:27:49 PM
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s=[]
        for i in nums:
            if i not in s:
                s.append(i)
            else:
                return i

        