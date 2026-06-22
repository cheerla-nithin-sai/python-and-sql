# Last updated: 6/22/2026, 7:54:43 AM
1class Solution:
2    def maxNumberOfBalloons(self, text: str) -> int:
3        d= Counter(text)
4        return min(d['b'],d['a'],d['n'],d['l']>>1,d['o']>>1)
5        
6