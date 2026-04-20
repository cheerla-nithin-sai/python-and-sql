# Last updated: 4/20/2026, 1:28:02 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if len(cost)<=2:
            return min(cost)
        dp=[0]*(len(cost))
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])