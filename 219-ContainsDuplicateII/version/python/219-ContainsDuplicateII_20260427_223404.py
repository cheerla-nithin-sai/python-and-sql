# Last updated: 4/27/2026, 10:34:04 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        d={}
4        for i in range(len(nums)):
5            if nums[i] in d and abs(i-d[nums[i]])<=k:
6                return True
7            else:
8                d[nums[i]]=i
9        return False
10
11
12        