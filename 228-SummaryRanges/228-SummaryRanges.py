# Last updated: 4/21/2026, 8:41:24 AM
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = []
        if len(nums)==0:
            return l
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]!=1:
                if start==nums[i-1]:
                    l.append(str(start))
                else:
                    l.append(f"{start}->{nums[i-1]}")
                start=nums[i]
        if start==nums[-1]:
            l.append(str(start))
        else:
            l.append(f"{start}->{nums[-1]}")
        return l