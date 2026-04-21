# Last updated: 4/21/2026, 8:41:18 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s))=="".join(sorted(t))
        