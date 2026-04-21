# Last updated: 4/21/2026, 8:42:29 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        return len(l[-1])
        