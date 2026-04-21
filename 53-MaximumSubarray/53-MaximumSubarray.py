# Last updated: 4/21/2026, 8:42:31 AM
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_sum=-sys.maxsize-1
        c_sum=0
        for i in range(len(nums)):
            c_sum+=nums[i]
            if c_sum>m_sum:
                m_sum=c_sum
            if c_sum<0:
                c_sum=0
            

        return m_sum
        