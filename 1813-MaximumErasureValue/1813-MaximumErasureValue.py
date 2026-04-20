# Last updated: 4/20/2026, 1:26:00 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        m=0
        c_s=0
        start=0
        num_set=set()
        for end in range(len(nums)):
            while nums[end] in num_set:
                num_set.remove(nums[start])
                c_s-=nums[start]
                start+=1
            c_s+=nums[end]
            num_set.add(nums[end])
            m=max(m,c_s)
        return m


        return m