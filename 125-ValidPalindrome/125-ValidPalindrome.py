# Last updated: 4/21/2026, 8:42:09 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        k="".join([i for i in s.lower() if i.isalnum()])

        return k==k[::-1]
        