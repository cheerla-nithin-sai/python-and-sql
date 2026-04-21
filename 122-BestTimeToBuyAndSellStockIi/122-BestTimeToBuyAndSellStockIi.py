# Last updated: 4/21/2026, 8:42:10 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        buy=float('inf')
        for price in prices:
            if price>buy:
                maxp+=price-buy
            buy=price
        return maxp

