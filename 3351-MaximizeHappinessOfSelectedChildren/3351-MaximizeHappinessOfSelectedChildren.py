# Last updated: 4/20/2026, 1:24:33 PM
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        h=0
        ron=0
        for i in range(k):
            h+=max(happiness[i]-ron,0)
            ron+=1
        return h


        