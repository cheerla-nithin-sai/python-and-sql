# Last updated: 4/20/2026, 1:25:58 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = 0
        l=[0]
        for i in gain:
            s+=i
            l.append(s)
        return max(l)
        