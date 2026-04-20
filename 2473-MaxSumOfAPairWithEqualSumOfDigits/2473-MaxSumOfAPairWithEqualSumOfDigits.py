# Last updated: 4/20/2026, 1:25:08 PM
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        s_sum=[0]*82
        ans=-1
        for i in nums:
            num_sum=sum(int(j) for j in str(i))
            if s_sum[num_sum]!=0:
                ans=max(ans,i+s_sum[num_sum])
            s_sum[num_sum]=max(i,s_sum[num_sum])
        return ans

        