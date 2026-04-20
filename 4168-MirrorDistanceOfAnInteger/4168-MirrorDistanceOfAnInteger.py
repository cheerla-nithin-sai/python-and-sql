# Last updated: 4/20/2026, 1:23:52 PM
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n-int(str(n)[::-1]))
        