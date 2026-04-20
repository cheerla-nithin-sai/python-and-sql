# Last updated: 4/20/2026, 1:27:53 PM
class Solution:
    def count_goal(self,nums,goal):
        l=0
        c=0
        sub_sum=0
        for r in range(len(nums)):
            sub_sum+=nums[r]
            while sub_sum>goal and l<=r:
                sub_sum-=nums[l]
                l+=1
            c+=r-l+1
        return c       
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        x=self.count_goal(nums,goal)
        y=self.count_goal(nums,goal-1)
        return x-y