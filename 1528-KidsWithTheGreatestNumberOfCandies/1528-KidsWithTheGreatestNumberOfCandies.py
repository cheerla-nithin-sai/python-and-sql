# Last updated: 4/20/2026, 1:26:24 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        l = []
        k = max(candies)
        for i in candies:
            l.append(i+e>=k)
        return l
        