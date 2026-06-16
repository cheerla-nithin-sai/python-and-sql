# Last updated: 6/16/2026, 11:08:38 AM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        ans=[[]]
4        nums.sort()
5        for num in nums:
6            ans+=[i+[num] for i in ans if i+[num] not in ans]
7        return ans