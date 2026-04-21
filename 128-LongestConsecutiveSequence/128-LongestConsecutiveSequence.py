# Last updated: 4/21/2026, 8:42:07 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s=sorted(set(nums))
        l=0
        k=[]
        for i in range(len(s)-1):
            if s[i]+1==s[i+1]:
                k.append(s[i])
                l=max(len(k),l)
            else:
                k=[]
        return l+1



        