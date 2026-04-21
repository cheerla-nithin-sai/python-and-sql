# Last updated: 4/21/2026, 8:41:19 AM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res=[]
        l,r=0,0
        while r<len(nums):
            while d and d[-1]<nums[r]:
                d.pop()
            d.append(nums[r])
            if r-l+1==k:
                res.append(d[0])
                if d[0]==nums[l]:
                    d.popleft()
                l+=1
            r+=1
        return res