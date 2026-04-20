# Last updated: 4/20/2026, 1:25:01 PM
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        l=-1
        num_set=set(nums)
        nums.sort()
        for i in nums:
            c=0
            num=i
            while num in num_set:
                num_set.remove(num)
                c+=1
                num=num*num
            l=max(c,l)
        return l if l>1 else -1
        