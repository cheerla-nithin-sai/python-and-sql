# Last updated: 4/20/2026, 1:23:50 PM
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1]+s[k:]
        