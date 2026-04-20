# Last updated: 4/20/2026, 1:26:19 PM
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=set([s[i:i+k] for i in range(len(s)-k+1)])
        return len(n)==2**k