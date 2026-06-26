# Last updated: 6/26/2026, 9:27:06 AM
1class Solution:
2    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
3        a=0
4        n=len(nums)
5        for i in range(n):
6            c=0
7            for j in range(i,n):
8                if target==nums[j]:
9                    c+=1
10                if c>(j-i+1)//2:
11                    a+=1
12        return a
13        