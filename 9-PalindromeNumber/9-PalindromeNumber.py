# Last updated: 4/21/2026, 8:42:55 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
        